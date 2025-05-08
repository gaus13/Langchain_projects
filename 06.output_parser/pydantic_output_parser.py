from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()


# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )

class Person(BaseModel):
    name: str = Field(description= 'Name of the person')
    age: int = Field(gt = 25, description= 'Age of the person ')
    city: str = Field(description='name of the city the person belongs to ')

# what is the use of this line of the code
parser = PydanticOutputParser(pydantic_object= Person)

template = PromptTemplate(
    template='Generate the name, and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}

)

prompt = template.invoke({'place': 'Indian'})
result = llm.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)
# print(prompt)

"""we can also use chain to simplify the code
chain = template | model| parser 
then in a variable store the chain.invoke """
