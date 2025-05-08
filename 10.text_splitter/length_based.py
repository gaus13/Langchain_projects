from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# this loads our doc from the pdf 
loader = PyPDFLoader('job_ds.pdf')


# text = """Artificial Intelligence (AI) is transforming the world in unprecedented ways. 
# From healthcare to transportation, AI systems are being integrated to improve efficiency and accuracy. 
# One of the most impactful advancements is the development of large language models like GPT, which can understand and generate human-like text.
#  These models are now used in chatbots, virtual assistants, content creation, and even coding.
# """

# for every page we get one doc object
doc = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0, #chunk overlap se uneven word split se jo context loose hoti hai we save it till some extent
    separator=' '
)

# result = splitter.split_text(text)
# print(result)

# now that we are using document to split text we will use split_document instead of above func


result = splitter.split_documents(doc)
print(result[2].page_content)