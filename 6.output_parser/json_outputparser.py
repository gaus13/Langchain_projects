# we cannot decide or enforce the schema of the json output in here llm decide itself

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()


# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )


parser = JsonOutputParser()

template1 = PromptTemplate(
    template='Give me a name, age and city of an indian cartoon character \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template1.format()
# result = llm.invoke(prompt)

# final_result = parser.parse(result.content)
# print(final_result)

chain = template1 | llm | parser

# while calling chain.invoke we must need to send a dict (empty bhi chalega)
result = chain.invoke({})
print(result)