import fitz

doc = fitz.Document("./data/studies_in_manuscript_cultures/36.pdf")

toc = doc.get_toc()[3:5]
print(toc)
for (level, title, start), (_,_,end) in zip(toc, toc[1:]):
    start -= 1
    end -= 1
    if start == end:
        continue
    pages = doc.pages(start, end)
    print(f"'{title}' from {start} to {end}") 
    
    blocks = [block[4] for block in next(pages).get_text("blocks")]
    formatted = ["".join(block.splitlines()) for block in blocks]
    print(formatted[1])
