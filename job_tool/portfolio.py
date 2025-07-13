import chromadb
import uuid

class Portfolio:
    def __init__(self):
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio_from_resume(self, resume_text):
        if not resume_text.strip():
            return
        doc_id = str(uuid.uuid4())
        self.collection.add(
            documents=[resume_text],
            metadatas=[{"source": "resume", "text": resume_text}],
            ids=[doc_id]
        )

    def query_links(self, skills):
        result = self.collection.query(query_texts=skills, n_results=2)
        return result.get('metadatas', [])
