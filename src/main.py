from src.chains.chat_chain import create_chat_assistant, get_response

def main():
    print("\n🤖 Personal Chat Assistant (Nova) is now running!")
    print("Type 'exit' to end the chat.\n")

    assistant = create_chat_assistant()

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Nova: Goodbye! Have a great day 👋")
            break

        response = get_response(assistant, user_input)
        print(f"Nova: {response}\n")


if __name__ == "__main__":
    main()
