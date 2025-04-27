from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)

# with the use of embed_query() we can ask/convert the vector of the given query
result = embedding.embed_query("Delhi is the capital of india ")
print(str(result))