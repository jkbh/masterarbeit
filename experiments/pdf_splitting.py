from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_transformers import EmbeddingsRedundantFilter
from langchain.vectorstores import Chroma

loader = PyMuPDFLoader("./data/studies_in_manuscript_cultures/36.pdf")

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100) 

documents = loader.load_and_split(splitter)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cuda"})
embeddings_filtered = EmbeddingsRedundantFilter(embeddings=embeddings, similarity_threshold=0.95 )

db = Chroma.from_documents(documents, embeddings)
