from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task= "text-generation"
)

model = ChatHuggingFace(llm =llm)

result = model.invoke("where is kalpa in India")

print(result.content)

# import os
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# # Load token from .env
# hf_token = os.getenv("HF_API_TOKEN")

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     huggingfacehub_api_token=hf_token
# )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke("what is opera house and why it was build")
# print(result.content)
