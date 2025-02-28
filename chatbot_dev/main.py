from chatbot import chatbot_response
from memory import load_existing_embeddings

load_existing_embeddings()

print("\nChatbot: Hi! Ask me anything. Type 'exit' to quit.\n")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}\n")
