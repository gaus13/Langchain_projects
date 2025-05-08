from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="people.csv")
docs = list(loader.lazy_load())  # Convert generator to list

print(len(docs))  # Now this works
for doc in docs:
    print(doc.page_content)
