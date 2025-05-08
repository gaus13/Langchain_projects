from langchain_community.document_loaders import PyPDFLoader 


loader = PyPDFLoader("job_ds.pdf")

doc = loader.load()

print(len(doc))
print(doc[0].page_content)
print(doc[1].metadata)