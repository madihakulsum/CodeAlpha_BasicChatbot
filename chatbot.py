def greet_user():
    print("🤖 ChatBot: Hello! I'm your friendly chatbot.")
    name = input("🤖 ChatBot: What's your name?\n You: ")
    print(f"🤖 ChatBot: Nice to meet you, {name}! Type 'bye' to end the chat.")
    return name

def generate_response(user_input, name):
    user_input = user_input.lower().strip()

    if user_input == "how are you":
        return "I'm doing great! 😊"
    elif user_input == "your name":
        return "I'm ChatBot — your digital friend."
    elif user_input == "motivate me":
        return "You’ve got this! Every big achievement starts with small steps."
    elif user_input == "what's the weather":
        return "I can’t see outside, but I hope it’s sunny where you are!"
    elif user_input == "what is python":
        return "Python is a programming language used for apps, AI, websites and more."
    elif user_input in ["thank you", "thanks", "thnx"]:
        return f"You're welcome, {name}!"
    else:
        return "I didn't understand that. Try asking something else!"

def chat():
    name = greet_user() 
    while True: 
        user_input = input(f"{name}: ")
        if user_input.lower().strip() == "bye":
            print(f"🤖 ChatBot: Goodbye, {name}!")
            break  
        response = generate_response(user_input, name)
        print(f"🤖 ChatBot: {response}")  
chat()