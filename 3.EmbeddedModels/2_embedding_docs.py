# here we have showm how we can process multiple query

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)

documents = [
    "Delhi is the capital of india ",
    "Paris is a be"
]

# with the use of embed_dociments() we can ask/convert tp the vector of multiple query
result = embedding.embed_documents("Delhi is the capital of india ")
print(str(result))