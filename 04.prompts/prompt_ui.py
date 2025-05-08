# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st
# import os
# from langchain_core.prompts import PromptTemplate

# # Load environment variables from .env file
# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task= "text-generation"
# )

# model = ChatHuggingFace(llm =llm)


# # Streamlit UI
# st.header("Research Tool")


# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


# # user_input = st.text_input("Enter your text:")

# # template
# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}  
# Explanation Length: {length_input}  
# 1. Mathematical Details:  
#    - Include relevant mathematical equations if present in the paper.  
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
# 2. Analogies:  
#    - Use relatable analogies to simplify complex ideas.  
# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=['paper_input', 'style_input','length_input'],
# validate_template=True
# )

# # filling the placeholders
# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input':style_input,
#     'length_input': length_input
# })


# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content)


# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_core.prompts import PromptTemplate

# # Load environment variables
# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task= "text-generation"
# )

# model = ChatHuggingFace(llm =llm)

# # Streamlit UI
# st.header("Research Tool")

# paper_input = st.selectbox(
#     "Select Research Paper Name",
#     [
#         "Attention Is All You Need",
#         "BERT: Pre-training of Deep Bidirectional Transformers",
#         "GPT-3: Language Models are Few-Shot Learners",
#         "Diffusion Models Beat GANs on Image Synthesis"
#     ]
# )

# style_input = st.selectbox(
#     "Select Explanation Style",
#     ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
# )

# length_input = st.selectbox(
#     "Select Explanation Length",
#     ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
# )

# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}  
# Explanation Length: {length_input}  
# 1. Mathematical Details:  
#    - Include relevant mathematical equations if present in the paper.  
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
# 2. Analogies:  
#    - Use relatable analogies to simplify complex ideas.  
# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
#     input_variables=["paper_input", "style_input", "length_input"],
# )

# prompt_text = template.format(
#     paper_input=paper_input,
#     style_input=style_input,
#     length_input=length_input
# )

# if st.button("Summarize"):
#     result = llm.invoke(prompt_text)
#     st.write(result)


from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate, load_prompt

# Load environment variables from .env file
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit UI
st.header("Research Tool")

# Check if API key exists in environment variables
if not groq_api_key:
    st.error("Groq API key not found in environment variables. Please add GROQ_API_KEY to your .env file.")
else:
    # Initialize Groq model
    llm = ChatGroq(
        api_key=groq_api_key,
        model_name="llama3-8b-8192"
    )
    
    paper_input = st.selectbox(
        "Select Research Paper Name",
        [
            "Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers",
            "GPT-3: Language Models are Few-Shot Learners",
            "Diffusion Models Beat GANs on Image Synthesis"
        ]
    )

    style_input = st.selectbox(
        "Select Explanation Style",
        ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
    )

    length_input = st.selectbox(
        "Select Explanation Length",
        ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
    )

    template = load_prompt('template.json')

    prompt = template.format(
        paper_input=paper_input,
        style_input=style_input,
        length_input=length_input
    )

    if st.button("Summarize"):
        with st.spinner("Generating summary..."):
            try:
                result = llm.invoke(prompt)
                st.write(result.content)
            except Exception as e:
                st.error(f"Error generating summary: {str(e)}")