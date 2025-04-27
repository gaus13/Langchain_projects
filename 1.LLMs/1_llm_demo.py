from langchain_openai import OpenAI
# dotenv apka secret keys ko load karta hai env file se
from dotenv import load_dotenv

# function ko invoke(jagaya ya bulaya)
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

# invoke function in langchain used to communicate with gpt model and ask questions.
result = llm.invoke("What is the capital of india")

# when run this code it ask llm model and return the ans
print(result)
