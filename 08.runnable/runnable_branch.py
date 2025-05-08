"""This is basically used where we need conditional logic 
we send tuples inside a runnable branch"""

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnableBranch, RunnablePassthrough

# Load environment variables
load_dotenv()

# Get Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq model
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama3-8b-8192",
    temperature=0  # Important to make output less random
)

prompt1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summarize the following text \n  {text}',
    input_variables=['topic']
)


