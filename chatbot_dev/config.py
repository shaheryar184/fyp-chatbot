import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

LLAMA_MODEL = os.getenv("LLAMA_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

FAISS_DIM = int(os.getenv("FAISS_DIM"))
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH")
