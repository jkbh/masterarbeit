from nltk import sent_tokenize
import fitz
from collections import Counter


def pdf_to_chunks(path):
    pass


def pdf_fulltext(path):
    with fitz.open(path) as document:
        text = chr(12).join([page.get_text() for page in document])
    return text


def pdf_thisthat(path):
    with fitz.open(path) as document:
        # for i, page in enumerate(document.pages()):
        page = document.load_page(24)
        blocks = page.get_text("dict", sort=True)["blocks"]
        for block in blocks:
            # for now, skip images
            if block["type"] == 0:
                size, font, text = join_block_texts(block)
                print(size)
                print(font)
                print(text)


def join_block_texts(block):
    sizes = []
    texts = []
    fonts = []
    for line in block["lines"]:
        for span in line["spans"]:
            texts.append(span["text"].strip("\n-"))
            sizes.append(span["size"])
            fonts.append(span["font"])

    size = Counter(sizes).most_common()[0][0]
    font = Counter(fonts).most_common()[0][0]
    text = "".join(texts)
    return size, font, text


class PDFSplitter:
    def __init__(self, chunksize):
        self.chunksize = chunksize

    def _load_fulltext(self, path):
        with fitz.open(path) as document:
            text = chr(12).join([page.get_text() for page in document])
        return text

    def process(self, path):
        text = self._load_fulltext(path)
        words = sent_tokenize(text)
        return words


if __name__ == "__main__":
    pdf_thisthat("./data/journal.pdf")
