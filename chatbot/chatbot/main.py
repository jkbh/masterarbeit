from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
import fitz
from operator import itemgetter
from llama_index.text_splitter import SentenceSplitter
from llama_index import Document
import logging
from vectorstore import Vectorstore
from nltk import sent_tokenize

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def preprocess_pdf(path):
    logger.info("processing pdf into documents")
    with fitz.open(path) as document:
        fulltext = chr(12).join([page.get_text() for page in document])

    splitter = SentenceSplitter(separator=".", chunk_size=128, chunk_overlap=20)

    sent_tokenize(fulltext)
    nodes = splitter.get_nodes_from_documents([Document(text=fulltext)])
    documents = [node.text for node in nodes]
    ids = [node.node_id for node in nodes]

    return ids, documents


def main():
    pdf_path = "./data/journal.pdf"
    model_path = "TheBloke/Mistral-7B-Instruct-v0.2-AWQ"

    ids, documents = preprocess_pdf(pdf_path)

    store = Vectorstore("~/dev/masterarbeit/chatbot/vectorstore.db")
    store.ingest(ids, documents)

    question = "What was special about prompt book use in the late nineteeth century in Hamburg?"
    results = store.query(query_texts=[question])["documents"]

    results = ["".join(result) for result in results]

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, low_cpu_mem_usage=True, device_map="cuda:0"
    )

    streamer = TextStreamer(tokenizer=tokenizer)
    chat = [
        {
            "role": "user",
            "content": "You are an expert in humanities research. You only give truthful answers.",
        },
        {
            "role": "assistant",
            "content": "Ok, I'm a truthful humanities expert, how can help you?",
        },
        {
            "role": "user",
            "content": "Answer the question using the following context: "
            + "\n".join(results)
            + "\n Question: "
            + question,
        },
    ]

    tokens = tokenizer.apply_chat_template(
        chat, add_generation_prompt=True, return_tensors="pt"
    ).cuda()

    _ = model.generate(tokens, streamer=streamer, max_new_tokens=512)


def get_pdf_font_info(document):
    font_counts = {}
    styles = {}

    for page in document:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] == 0:
                for line in block["lines"]:
                    for span in line["spans"]:
                        size = span["size"]
                        identifier = f"{size}"
                        styles[identifier] = {
                            "size": size,
                            "font": span["font"],
                        }

                        font_counts[identifier] = font_counts.get(identifier, 0) + 1
    font_counts = sorted(font_counts.items(), key=itemgetter(1), reverse=True)
    return font_counts, styles


def get_font_tags(counts, styles):
    paragraph_style = styles[counts[0][0]]
    paragraph_size = paragraph_style["size"]

    font_sizes = sorted([float(size) for size, count in counts], reverse=True)
    size_tag = {}
    idx = 0
    for size in font_sizes:
        idx += 1
        if size == paragraph_size:
            idx = 0
            size_tag[size] = "<p>"
        elif size > paragraph_size:
            size_tag[size] = f"<h{idx}>"
        elif size < paragraph_size:
            size_tag[size] = f"<s{idx}>"

    return size_tag


def get_tagged_doc(document, tags):
    tagged_blocks = []
    first = True
    previous_span = {}

    for page in document:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] == 0:
                text = ""
                for line in block["lines"]:
                    for span in line["spans"]:
                        if span["text"].strip():
                            if first:
                                previous_span = span
                                first = False
                                text = tags[span["size"]] + span["text"]
                            else:
                                if span["size"] == previous_span["size"]:
                                    if text and all((c == "|") for c in text):
                                        # block_string only contains pipes
                                        text = tags[span["size"]] + span["text"]
                                    if text == "":
                                        # new block has started, so append size tag
                                        text = tags[span["size"]] + span["text"]
                                    else:  # in the same block, so concatenate strings
                                        text += " " + span["text"]

                                else:
                                    tagged_blocks.append(text)
                                    text = tags[span["size"]] + span["text"]

                                previous_span = span

                    # new block started, indicating with a pipe
                    text += "|"

                tagged_blocks.append(text)
    return tagged_blocks


def get_paragraphs_with_context(blocks, tags):
    paragraphs = []
    current_context = {tag: "" for tag in tags.values()}
    for block in blocks:
        for tag in current_context.keys():
            if block.startswith(tag):
                current_context[tag] = block
                if tag == "<p>":
                    paragraphs.append(current_context.copy())
                    break

    return paragraphs


def make_context_string(context):
    texts = [
        text.split(">")[1] for tag, text in context.items() if text and "s" not in tag
    ]
    cleaned = [text.replace("|", "").strip() for text in texts]
    return " > ".join(cleaned)


if __name__ == "__main__":
    # pdf_path = "./data/journal.pdf"
    # with fitz.open(pdf_path) as pdf:
    #     counts, styles = get_pdf_font_info(pdf)
    #     tags = get_font_tags(counts, styles)
    #     blocks = get_tagged_doc(pdf, tags)
    #     contexts = get_paragraphs_with_context(blocks, tags)
    #     print(make_context_string(contexts[200]))
    main()


# llm = Llama(
#     model_path="./models/llama-2-13b-chat.Q5_K_M.gguf", n_gpu_layers=41, verbose=False
# )

# output_stream = llm.create_chat_completion(
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a football enthuisast that can't hide their extreme exitement towards the game. You love to answer in Gen-Z style language. You root for the english team and make a big deal out of it whenever you can.",
#         },
#         {
#             "role": "user",
#             "content": "Please give me a list of persons that have coached the german national football team",
#         },
#     ],
#     stream=True,
# )
#
# texts = []
# for item in output_stream:
#     text = item["choices"][0]["delta"].get("content", "")
#     texts.append(text)
#     print(text, end="")
#
# response = "".join(texts)
# print(response)
