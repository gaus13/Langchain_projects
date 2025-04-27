from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
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
    template= 'Generate a tweet about {topic}',
    input_variables= ['topic']
)


prompt2 = PromptTemplate(
    template= 'Generate a Linkedin post about {topic}',
    input_variables= ['topic']
)

parser = StructuredOutputParser()

# you initialize runnable parallel as dictionary 
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1 , llm, parser),
    ' '
})