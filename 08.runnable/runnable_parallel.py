from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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

# Define the prompts
prompt1 = PromptTemplate(
    template= 'Generate a tweet and a LinkedIn post about {topic}. Return the output as a JSON object with keys "tweet" and "linkedin": {{ "tweet": "<tweet_text>", "linkedin": "<linkedin_text>" }}',
    input_variables= ['topic']
)

# Define the parallel chain
parallel_chain = RunnableParallel({
    'content': RunnableSequence(prompt1, llm)
})

# Invoke the parallel chain and get the result
result = parallel_chain.invoke({'topic': 'AI'})

# Extract and clean up the output (just the tweet and linkedin)
response_content = result['content'].content

# Extract the JSON-like content from the raw message
start = response_content.find("{")
end = response_content.rfind("}") + 1
clean_json = response_content[start:end]

# Print only the relevant output (tweet and linkedin)
print("Cleaned Output:", clean_json)


