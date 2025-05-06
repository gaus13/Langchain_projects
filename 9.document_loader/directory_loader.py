from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path ='books', #ye path wo folder hai jahan sabhi files padi hai
    glob='*.pdf', #btata hai glob ki kis type ki file load karni hai in folder se
    loader_cls= PyPDFLoader #kis class type ki file hai wo btaya
)

docs = loader.load()

print(len(docs))