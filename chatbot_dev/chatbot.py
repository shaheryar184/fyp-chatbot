from transformers import pipeline
from config import LLAMA_MODEL
from memory import retrieve_past_chats, embedder, add_embedding_to_faiss
from database import store_chat, get_chat_by_index

llama_pipeline = pipeline("text-generation", model=LLAMA_MODEL)

def chatbot_response(user_input):
    past_chat_indices = retrieve_past_chats(user_input, k=3)
    past_chats = [get_chat_by_index(idx) for idx in past_chat_indices if get_chat_by_index(idx)]

    prompt = "You are a chatbot that remembers past conversations.\n\n"
    if past_chats:
        prompt += "Previous Conversations:\n"
        for chat in past_chats:
            prompt += f"- User: {chat['user_message']}\n  Bot: {chat['bot_response']}\n"

    prompt += f"\nUser: {user_input}\nBot:"
    response = llama_pipeline(prompt, max_length=150, do_sample=True)[0]["generated_text"]
    bot_reply = response.split("Bot:")[-1].strip()

    embedding = embedder.encode(user_input).tolist()
    faiss_index = add_embedding_to_faiss(embedding)
    store_chat(faiss_index, user_input, bot_reply, embedding)

    return bot_reply
