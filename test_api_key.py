import openai
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

def test_api_key():
    try:
        llm = OpenAI(api_key=openai.api_key)

        response = llm("Hello, world!")
        print("API key is valid.")
        print("Response:", response)
    except openai.error.AuthenticationError as e:
        print("API key is invalid:", str(e))
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    test_api_key()
