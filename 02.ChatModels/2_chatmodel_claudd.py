from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# temp is tone of output you want and max_compl_token is max words/tokens u want in ans. 
model = ChatAnthropic ( model='claude- 3.5-sonet-20241022')

result = model.invoke("What is opera house ")

# by just printing the result it give a lot of metadata so we fetch only content this way
print(result)