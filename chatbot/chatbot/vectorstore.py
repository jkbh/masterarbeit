from chromadb import PersistentClient
from chromadb.embedding_functions import SentenceTransformerEmbeddingFunction
from logging import getLogger

logger = getLogger(__name__)


class Vectorstore:
    def __init__(self, path):
        self._client = PersistentClient(path)
        self._embedding_function = SentenceTransformerEmbeddingFunction(device="cuda")
        logger.debug(f"initialised vectorstore at {path}")

    def ingest(self, ids, documents, collection_name="default"):
        collection = self._client.get_or_create_collection(
            name=collection_name,
            embedding_function=self._embedding_function,
        )

        collection.add(ids=ids, documents=documents)
        logger.debug(f"added {len(ids)} documents to collection: {collection_name}")

    def query(self, query, collection="default"):
        collection = self._client.get_collection(
            name=collection, embedding_function=self._embedding_function
        )
        results = collection.query(
            query_texts=[query], n_results=5, include=["documents"]
        )
        return results
