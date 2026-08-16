import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")


client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)


def get_args():
    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def get_response(prompt: str):
    messages: list[ChatCompletionMessageParam] = [
        {
            "role": "user",
            "content": prompt,
        }
    ]

    response = client.chat.completions.create(
        messages=messages, model="openrouter/free"
    )

    if response is None:
        raise RuntimeError("No response received")

    if response.usage is None:
        raise RuntimeError("Missing usage metadata")

    return response


def print_response(response, args):
    if args.verbose:
        print(
            f"User prompt: {args.user_prompt}",
            f"Prompt tokens: {response.usage.prompt_tokens}",
            f"Response tokens: {response.usage.completion_tokens}",
            sep="\n",
        )

    print(
        response.choices[0].message.content,
    )


def main():
    args = get_args()
    response = get_response(args.user_prompt)
    print_response(response, args)


if __name__ == "__main__":
    main()
