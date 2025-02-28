import pymongo
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

collection.create_index([("embedding", pymongo.HASHED)])

def store_chat(faiss_index, user_message, bot_response, embedding):
    collection.insert_one({
        "faiss_index": faiss_index,
        "user_message": user_message,
        "bot_response": bot_response,
        "embedding": embedding
    })

def get_all_embeddings():
    return list(collection.find({}, {"_id": 0, "embedding": 1}))

def get_chat_by_index(index):
    return collection.find_one({"faiss_index": index}, {"_id": 0, "user_message": 1, "bot_response": 1})
