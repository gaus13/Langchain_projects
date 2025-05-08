"""It is a runnable premitive that allows you to apply custom python functions withIN an AI pipeline
it acts as a middleware between diff ai components enabling preprocessing 
transformation, api calls, filtering and post-processing in a langchain workflow"""

# THIS IS AN EXAMPLE OF HOW RUNNABLE LAMBDA WORKS
# from langchain.schema.runnable import RunnableLambda

# def word_count(text):
#     return len(text.split())

# runnable_word_count = RunnableLambda(word_count)

# print(runnable_word_count.invoke('Hi my name is danish and i dont know where i am'))


"""kisi bhi custom logic add karne ke liye we can use this runnable """