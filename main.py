import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.config import system_prompt,model_name

def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    has_verbose = '--verbose' in args

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client, messages, has_verbose=has_verbose)


def generate_content(client, messages,has_verbose=False):
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    if has_verbose:
        print("User prompt:",messages)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)



if __name__ == "__main__":
    main()


