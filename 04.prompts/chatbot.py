from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq modelcd 
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )

# made this list to store all the prev msg by the llm
chat_history = [
    SystemMessage(content='you are a very helpful AI assistant')
]

# as in chatbot the prog will keep on executing till it exits thus we're using while loop

while True:
    user_input = input ('YOU: ')
    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        break

    result = llm.invoke(chat_history)

    # ye ai messg and human msg lable karne se ye fayda hai ki humein aur llm ko pta chalta hai kaun kiski baat h 
    chat_history.append(AIMessage(content= result.content))
    print("AI: ", result.content)

print(chat_history)