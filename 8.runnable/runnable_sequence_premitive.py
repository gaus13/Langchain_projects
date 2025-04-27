# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema
# from langchain.schema.runnable import RunnableSequence, RunnableLambda

# load_dotenv()

# # Get Groq API key from environment variables
# groq_api_key = os.getenv("GROQ_API_KEY")

#  # Initialize Groq model
# llm = ChatGroq(
#     api_key=groq_api_key,
#     model_name="llama3-8b-8192",
#     temperature=0  # Very important for strict JSON output
# )



# # Define the structured output you expect
# response_schemas = [
#     ResponseSchema(name="joke", description="A funny joke related to the given topic")
# ]


# parser = StructuredOutputParser(response_schemas=response_schemas)

# # # New prompt: very clear instruction
# # prompt1 = PromptTemplate(
# #     template="""Write a joke about {topic}.
# # Respond only in JSON format like this:
# # {{"joke": "your joke here"}}""",
# #     input_variables=['topic']
# # )

# prompt1 = PromptTemplate(
#     template="""You must only respond in raw JSON format. No extra words, no explanation.
# Strictly output like this:

# 	{{ "joke": "your joke here" }}

# Write a joke about the topic: {topic}""",
#     input_variables=['topic']
# )


# # Transform step: map "joke" -> "text"
# def map_joke_to_text(parsed_output):
#     return {"text": parsed_output["joke"]}


# prompt2 = PromptTemplate(
#     template= 'explain the following joke - {text}',
#     input_variables=['text']

# )

# chain = RunnableSequence(prompt1, llm, parser, RunnableLambda(map_joke_to_text),   prompt2, llm, parser)

# result = (chain.invoke({'topic': 'Bihar'}))
# print(result)


from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema, OutputFixingParser
from langchain.schema.runnable import RunnableSequence, RunnableLambda

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

# Define expected structured output
response_schemas = [
    ResponseSchema(name="joke", description="A funny joke related to the given topic")
]

# Safe parser that auto-fixes small LLM mistakes
parser = OutputFixingParser.from_llm(llm=llm, parser=StructuredOutputParser(response_schemas=response_schemas))

# Very strict and serious prompt
prompt1 = PromptTemplate(
    template="""You MUST only respond in raw JSON format. 
No extra words, no explanation, no Markdown, no code blocks. 

STRICTLY output exactly like this: 

{{ "joke": "your joke here" }}

Now, write a joke about the topic: {topic}""",
    input_variables=['topic']
)

# Transform step: map "joke" -> "text"
def map_joke_to_text(parsed_output):
    return {"text": parsed_output["joke"]}

# Second prompt to explain the joke
prompt2 = PromptTemplate(
    template='Explain the following joke clearly - {text}',
    input_variables=['text']
)

# Create the runnable sequence
chain = RunnableSequence(
    prompt1,
    llm,
    parser,
    RunnableLambda(map_joke_to_text),
    prompt2,
    llm,
)

# Invoke the chain
result = chain.invoke({'topic': 'Bihar'})
print(result.content)


