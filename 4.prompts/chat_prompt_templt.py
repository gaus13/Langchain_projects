from langchain_core.prompts import ChatPromptTemplate

Chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}' )

]) 

prompt = Chat_template.invoke({'domain':'cricket', 'topic':'off side'})

print(prompt)