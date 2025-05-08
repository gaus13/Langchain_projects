# """this is a special runnable which returns the input as output without 
# and modification"""


# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema, OutputFixingParser
# from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough

# # Load environment variables
# load_dotenv()

# # Get Groq API key
# groq_api_key = os.getenv("GROQ_API_KEY")

# # Initialize Groq model
# llm = ChatGroq(
#     api_key=groq_api_key,
#     model_name="llama3-8b-8192",
#     temperature=0  # Important to make output less random
# )


# # Define what the output structure should be
# response_schemas = [
#     ResponseSchema(name="joke", description="A joke about the topic"),
# ]

# # Create the parser with the schema
# parser = StructuredOutputParser.from_response_schemas(response_schemas)

# prompt1= PromptTemplate(
#     template='write a joke about {topic}',
#     input_variables=['topic']
# )



# prompt2= PromptTemplate(
#     template='explain the following joke {text}',
#     input_variables=['text']
# )

# joke_gen_chain = RunnableSequence(prompt1, llm, parser)

# parallel_chain = RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'explaination': RunnableSequence(prompt2, llm, parser)
# })

# final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# # passthrough = RunnablePassthrough()
# # print(passthrough.invoke({'name':'danish'}))

# print(final_chain.invoke({'topic':'india'}))

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

# Load environment variables
load_dotenv()

# Get Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama3-8b-8192",
    temperature=0
)

# Define the response schema
response_schemas = [
    ResponseSchema(name="joke", description="The joke about the topic")
]

# Create the parser
parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Updated prompt to force JSON output
prompt1 = PromptTemplate(
    template='''
Write a joke about {topic}.
Respond ONLY in JSON format like this:
{{
    "joke": "<your joke here>"
}}
''',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='''
Explain this joke in simple words: {joke}.
Respond ONLY in JSON format like this:
{{
    "joke": "<joke explanation here>"
}}
''',
    input_variables=['joke']
)

# Define chains
joke_gen_chain = RunnableSequence(prompt1, llm, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, llm, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# Run
print(final_chain.invoke({'topic': 'india'}))
 