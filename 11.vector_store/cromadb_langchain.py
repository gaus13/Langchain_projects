from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Initialize the embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Sample documents to store in Chroma
texts = [
    "Groq is a fast LLM inference engine",
    "LangChain simplifies LLM workflows"
]

# Create a Chroma vector store
vectorstore = Chroma.from_texts(texts, embedding_model)

# Test similarity search
results = vectorstore.similarity_search("What is Groq?", k=1)
print(results[0].page_content)
