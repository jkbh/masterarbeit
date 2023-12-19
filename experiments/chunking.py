import pdfplumber
from collections import Counter


def get_header_font_size(pdf_path):
    fontsize_counter = Counter()
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words(extra_attrs=["fontname", "size"])
            lines = group_words_by_line(words)

        for words in lines.values():
            fontsize_counter[words[0]["size"]] += 1

        sizes = [size for size, count in fontsize_counter.items() if count > 1]
        print(sizes)


def group_words_by_line(words):
    lines = {}
    for word in words:
        line = word["top"]
        if line not in lines:
            lines[line] = []
        lines[line].append(word)
    return lines


pdf_path = "./data/studies_in_manuscript_cultures/36.pdf"
get_header_font_size(pdf_path)
