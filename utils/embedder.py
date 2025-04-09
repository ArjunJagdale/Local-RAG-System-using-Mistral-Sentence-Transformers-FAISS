from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import textwrap

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.chunks = []
        self.chunk_embeddings = []

    def split_text(self, text, max_words=100):
        sentences = text.split(".")
        chunk = ""
        for s in sentences:
            if len(chunk.split()) + len(s.split()) < max_words:
                chunk += s + ". "
            else:
                self.chunks.append(chunk.strip())
                chunk = s + ". "
        if chunk:
            self.chunks.append(chunk.strip())

    def index_documents(self, text):
        self.split_text(text)
        self.chunk_embeddings = self.model.encode(self.chunks)
        self.index.add(np.array(self.chunk_embeddings))

    def retrieve_context(self, query, top_k=3):
        q_emb = self.model.encode([query])
        distances, indices = self.index.search(np.array(q_emb), top_k)
        return "\n".join([textwrap.fill(self.chunks[i], width=80) for i in indices[0]])
