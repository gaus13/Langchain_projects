from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

# runnable lamba converts lambda func to runnable this we can use it in chain

load_dotenv()


# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give a sentiment of the feedback') 

parser2 = PydanticOutputParser(pydantic_object= Feedback)


prompt_one = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}

)

parser = StrOutputParser()

classifier_chain = prompt_one | llm | parser2

prompt_two = PromptTemplate(
    template='write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt_three = PromptTemplate(
    template='write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# result = classifier_chain.invoke({'feedback':'Netflix webseries Stranger things is the best webseries ever made i love it'})
# print(result)

# runnable branch mein we send multiple tuples acts like a "switch-case" or if-elif-else logic for chains.

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt_two | llm | parser),
    (lambda x:x.sentiment == 'negative', prompt_three | llm | parser),
    RunnableLambda(lambda x: 'Could not find any sentiment you are ded')


)

chain = classifier_chain | branch_chain
result = chain.invoke({'feedback': "this is a stupid phone"})
print(result)