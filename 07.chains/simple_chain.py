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

prompt = PromptTemplate(
    template='Generate 5 intresting facts about the given {topic}',
    input_variables=['topic']

)

parser = StrOutputParser()
chain = prompt | llm | parser

result = chain.invoke({'topic': 'T- 20 cricket'})

print(result)

# below func visualize the chain (chain draw kar deta hai)
chain.get_graph().print_ascii()