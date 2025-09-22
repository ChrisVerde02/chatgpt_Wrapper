import os
from dotenv import load_dotenv
from chatgpt_wrapper import ChatGPTWrapper

def main():
    # Load .env file
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env")

    bot = ChatGPTWrapper(api_key)

    print("Chat started. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        answer = bot.ask(user_input)
        print("Bot:", answer)

if __name__ == "__main__":
    main()