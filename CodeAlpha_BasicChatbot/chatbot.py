def get_response(user_input):
    """Return a predefined response based on normalized user input."""
    normalized = user_input.strip().lower()

    if normalized == "hello":
        return "Hi!"
    elif normalized == "how are you":
        return "I'm fine, thanks!"
    elif normalized == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def display_welcome():
    """Display the welcome banner and instructions."""
    print("================================")
    print("        BASIC CHATBOT")
    print("================================")
    print()
    print("Bot: Hello! Welcome to the chatbot.")
    print('Bot: Type "bye" to exit.')
    print()


def main():
    """Run the chatbot conversation loop until the user says bye."""
    display_welcome()

    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            print()
            break

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.strip().lower() == "bye":
            break

    print()
    print("Chat ended.")


if __name__ == "__main__":
    main()
