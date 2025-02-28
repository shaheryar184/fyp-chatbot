import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from config import FAISS_DIM, FAISS_INDEX_PATH, EMBEDDING_MODEL
from database import get_all_embeddings

embedder = SentenceTransformer(EMBEDDING_MODEL)
faiss_index = faiss.IndexHNSWFlat(FAISS_DIM, 32)

def save_faiss():
    faiss.write_index(faiss_index, FAISS_INDEX_PATH)

def load_faiss():
    if os.path.exists(FAISS_INDEX_PATH):
        return faiss.read_index(FAISS_INDEX_PATH)
    return faiss.IndexHNSWFlat(FAISS_DIM, 32)

faiss_index = load_faiss()

def load_existing_embeddings():
    stored_embeddings = [np.array(doc["embedding"]) for doc in get_all_embeddings()]
    if stored_embeddings:
        embeddings_matrix = np.vstack(stored_embeddings)
        faiss_index.add(embeddings_matrix)

def add_embedding_to_faiss(embedding):
    faiss_index.add(np.array(embedding).reshape(1, -1))
    save_faiss()
    return faiss_index.ntotal - 1

def retrieve_past_chats(query, k=3):
    if faiss_index.ntotal == 0:
        return []
    query_embedding = embedder.encode(query).reshape(1, -1)
    _, indices = faiss_index.search(query_embedding, k)
    return [int(idx) for idx in indices[0]]
