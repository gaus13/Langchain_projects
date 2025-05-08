# from langchain_huggingface.llms import HuggingFaceEndpoint
# from langchain_huggingface import ChatHuggingFace
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

# OLD (causes error)
# from langchain_huggingface.llms import HuggingFaceEndpoint
# from langchain_groq import ChatGroq

# NEW (correct)

from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )


# 1st prompt: detailed report
template1= PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)


# 2nd prompt: summary
template2= PromptTemplate(
    template="write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'ganga'})

result = llm.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result_final = llm.invoke(prompt2)
print(result_final.content)