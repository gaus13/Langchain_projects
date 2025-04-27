from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )

prompt_one = PromptTemplate(
    template='Generate a detailed report about the given {topic}',
    input_variables=['topic']

)

prompt_two = PromptTemplate(
    template='Extract the 5 most important points from the following text \n  {text}',
    input_variables=['text']

)

parser = StrOutputParser()

chain = prompt_one | llm | parser | prompt_two | llm | parser

result = chain.invoke({'topic':'Netflix webseries Stranger things'})
print(result)