#This is an example of typedict but not good for data validation

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()


# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )

# schema (also shown pydantic way of writing class)
class Review(BaseModel):

    key_themes: list[str] = Field(description= "write down all the key themes or points mentioned in the review in list")
    summary: str = Field(description= "A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description= "Generate the sentiment based on review which could be positve, negative or neutral")
    pros: Optional[list[str]] = Field(default=None, description= "write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description= "write down all the cons inside a list")
    name: Optional[str]= Field(default=None, description="Write down the name of the reviewer")


    """{This is a type dict method of schema setting} 
    key_themes: Annotated[list[str], "write down all the key themes or points mentioned in the review in list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Generate the sentiment based on review which could be positve, negative or neutral"]
    pros: Annotated[Optional[list[str]], "write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "write down all the cons inside a list"]"""


structued_model = llm.with_structured_output(Review)    

review_result = structued_model.invoke('''Reviewer: Ayesha Patel, I recently purchased the SoundBoom Mini Bluetooth Speaker, and I must say, it exceeded all my expectations. Despite its compact size, the sound quality is incredibly rich with surprisingly deep bass and crisp treble. The build feels premium, and its minimal, modern design fits perfectly on my work desk.
 Battery life is impressive too—I got nearly 10 hours of playback on a single charge. It paired seamlessly with my phone, and the connection remained stable throughout. For the price, this speaker is an absolute steal. I highly recommend it to anyone looking for powerful, portable audio on a budget.
''')

print(review_result.summary)