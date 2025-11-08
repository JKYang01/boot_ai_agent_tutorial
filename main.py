import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.call_function import call_function
from functions.config import (model_name,
                              MAX_ITERS,
                              system_prompt,
                              available_functions,
                              MAX_CHARS)

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

    # Remove --verbose from args before creating the user prompt
    prompt_args = [arg for arg in args if arg != '--verbose']
    user_prompt = " ".join(prompt_args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    j = 0
    while True:
        j+=1
        if j > MAX_ITERS:
            print("Maximum number of iterations reached, exiting.")
            sys.exit(1)
        try:
            result = generate_content(client, messages, has_verbose=has_verbose)
            if result:
                print(result)
                break
        except Exception as e:
            print("Error generating content:", e)

def generate_content(client, messages, has_verbose=False):
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],
                                           system_instruction=system_prompt),
    )
    # Add model's function calls to messages
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)
    if has_verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return response.text

    function_responses = []
    # Execute each function and collect results
    for call in response.function_calls:
        function_call_result = call_function(call, verbose=has_verbose)
        if not function_call_result.parts or not function_call_result.parts[0].function_response:
            raise Exception("Empty Function call")

        if has_verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        # Only append the Part object, not the entire Content
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function response generated, exiting.")

    # Add function result to messages
    messages.append(types.Content(role="user", parts=function_responses))
    return None

if __name__ == "__main__":
    main()


