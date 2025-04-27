from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# if you want same output everytime them set temp=0, as temp inc the variation in output inc
# and max_compl_token is max words/tokens u want in ans. 
model = ChatOpenAI( model='gpt-4', temperature= 0.6, max_completion_tokens= 10 )

result = model.invoke("What is opera house ")

# by just printing the result it give a lot of metadata so we fetch only content this way
print(result.content)