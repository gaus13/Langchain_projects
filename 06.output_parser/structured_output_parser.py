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

schema = [
    ResponseSchema(name = 'fact-1', description='Fact 1 about the topic'),
    ResponseSchema(name = 'fact-2', description='Fact 2 about the topic'),
    ResponseSchema(name = 'fact-3', description='Fact 3 about the topic'),

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables= {'format_instruction': parser.get_format_instructions()}
)

"""or we can write using chains like:
chain = template | model | parser
result = chain.invoke({'topic': 'Brack Obama' })
print(result)
"""
prompt = template.invoke({'topic': 'Brack Obama' })
result = llm.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)


# disAdvantages: schema to dega, but no data validation allowed/available
