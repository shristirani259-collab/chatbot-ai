print("=========================================")
print(" Rule-Based AI Chatbot")
print("=========================================")
print("Type 'bye', 'exit',or 'quit' to end the chat.")
print()

while True:
    user_input = input("you:").lower().strip()

    # Exit commands
    if user_input in ["bye", "exit","quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    # Greetings
    elif user_input in ["hello", "hi", "hey","hii"]:
        print("Bot: Hello! HOW can i help you?")

        #Asking about the bot
    elif"your name" in user_input or "who are you" in user_input:
        print("Bot: i am a simple Rule-Based AI Chatbot.")

        #Asking how the bot is
    elif"how are you" in user_input:
        print("Bot:i'm doing great! Thanks for askig.")

        # Help
    elif"Help" in user_input:
        print("Bot: You can greet me, ask my  name,ask how i am , or say bye.")

        # Thanks
    elif"thanks" in user_input:
        print("Bot:You're welcome!")

        # Default response 
    else:
        print("Bot: Soory, i don't understand that. Please try another question.")
  