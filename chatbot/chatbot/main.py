import logging
import fitz
from torch import cuda
from llama_index.text_splitter import SentenceSplitter
from llama_index import Document
from chatbot.vectorstore import Vectorstore
from chatbot.providers import MistralClient, OpenAIClient

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
device = "cuda" if cuda.is_available() else "cpu"

def preprocess_pdf(path):
    logger.info("processing pdf into documents")
    with fitz.open(path) as document:
        fulltext = chr(12).join([page.get_text() for page in document])

    splitter = SentenceSplitter(separator=".", chunk_size=128, chunk_overlap=20)

    nodes = splitter.get_nodes_from_documents([Document(text=fulltext)])
    documents = [node.text for node in nodes]
    ids = [node.node_id for node in nodes]

    return ids, documents


def main():
    store = Vectorstore("chatbot/vectorstore.db")

    # TODO: add logic to only preprocess pdf if it hasn't been done before
    # pdf_path = "chatbot/data/mc19-full.pdf"
    # ids, documents = preprocess_pdf(pdf_path)
    # store.ingest(ids, documents)

    question = "What was special about prompt book use in the late nineteeth century in Hamburg?"
    # question = "What is the difference between a prompt book and a prompt copy?"
    # question = "Who was the first person to use a prompt book?"
    results = store.query(query_texts=[question])["documents"][0]

    results = [
        f"{i}. " + result.replace("\n", "").strip()
        for i, result in enumerate(results, 1)
    ]

    chat = [
        {
            "role": "user",
            "content": "You are an expert in humanities research. You only give truthful answers that are grounded in the provided context.",
        },
        {
            "role": "assistant",
            "content": "Ok, I'm a truthful humanities expert that answers based on given context, how can I help you?",
        },
        {
            "role": "user",
            "content": "Answer the question using the sources given in the context.\n"
            + "Context:\n"
            + "\n".join(results)
            + "\nQuestion: "
            + question,
        },
    ]

    client = MistralClient() if cuda.is_available() else OpenAIClient()
    completition = client.get_chat_completition(chat)
    print(completition)


if __name__ == "__main__":
    main()
