from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os 

load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )
prompt = PromptTemplate( 
    template='Write a short and important summery in around 5 lines from the give text \n {eassy}',
    input_variables=['eassy']
)

loader = TextLoader('japan.txt', encoding='utf-8')


docs = loader.load()

parser = StrOutputParser()

# print(docs)

# prints the file content
# print(docs[0].page_content)

# below simple python code prints the meta data
# print(docs[0].metadata)

chain = prompt | llm | parser
ans = chain.invoke({"eassy": docs[0].page_content})
print(ans)