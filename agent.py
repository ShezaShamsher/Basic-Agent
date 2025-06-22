from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

Client = AsyncOpenAI(
    api_key= GEMINI_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"

)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful Assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=Client)
)

query = input("Enter your Query: ")

result = Runner.run_sync(
    agent,
    query
)

print(result.final_output)