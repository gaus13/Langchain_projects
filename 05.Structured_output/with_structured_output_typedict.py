#This is an example of typedict but not good for data validation

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()


# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

 # Initialize Groq model
llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )

# schema
class Review(TypedDict):

    key_themes: Annotated[list[str], "write down all the key themes or points mentioned in the review in list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Generate the sentiment based on review which could be positve, negative or neutral"]
    pros: Annotated[Optional[list[str]], "write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "write down all the cons inside a list"]


structued_model = llm.with_structured_output(Review)    

review_result = structued_model.invoke('''I recently bought the SoundBoom Mini, and I’m genuinely impressed. For such a small device, it delivers surprisingly loud and clear sound with deep bass. The battery life is solid—I get around 10 hours of playback on a single charge. It pairs instantly with my phone and has a sleek, minimal design that looks great on my desk.

Overall, it's perfect for casual listening, especially for the price. Highly recommended for anyone who wants portable, quality sound without breaking the bank!''')

print(review_result)