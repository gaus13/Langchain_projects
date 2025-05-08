

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
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

# prompt1 = template1.invoke({'topic': 'ganga'})

# result = llm.invoke(prompt1)

# prompt2 = template2.invoke({'text':result.content})

# result_final = llm.invoke(prompt2)
# print(result_final.content)

# here it is shown the use of output parser and chains
parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser
result = chain.invoke({'topic':"Manali himachal pradesh"})
print(result)