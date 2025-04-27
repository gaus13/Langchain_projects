from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# fetching groq api key from env variable 
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model (You are creating an instance of the ChatGroq model (basically connecting to Groq’s server)
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )

# creating a prompt
prompt = PromptTemplate(
    input_variables=['topic'],    #defines what input is needed
    template="suggest a catchy blog title about {topic}."

)


# create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# run the chain with a specific topic
topic = input('Enter a topic')
output = chain.run(topic)

print("Generate Blog Title", output)