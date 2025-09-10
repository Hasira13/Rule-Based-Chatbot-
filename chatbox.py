def chatbot():
    print("Chatbot: Hello! I'm a simple rule-based chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        # Rule-based responses
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot built with Python.")
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather right now, but it's always sunny in my code world!")
        elif "time" in user_input:
            from datetime import datetime
            print("Chatbot: The current time is", datetime.now().strftime("%H:%M:%S"))
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
chatbot()