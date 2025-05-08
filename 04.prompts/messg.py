from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )

# human messg jo user llm ko bhjta hai, ai jo reply deta wo ai messg, 
# system messg wo hai jo hum ai ko start mein dete hai like "you are a good doctor or helpfull assistant"

messages = [
    SystemMessage(content='You are a very helpful assistant'),
    HumanMessage(content='tell me about langchain')

]

result = llm.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
