# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = OpenAI(api_key="AIzaSyCr66WGD8DdV6H3p76V6S1dzVGBs-3fHYg")

# def query_llm_with_context(query: str, context: str):
#     system_content = """You are a helpful assistant for answering te user's questions."""

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": system_content},
#             {"role":"user", "content": f"Query: {query}\n\nContext:\n{context}"}
#         ],
#         temperature=0.4       
#     )
#     return response.choices[0].message.content




from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key="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"
)

MODEL_NAME = "gpt-3.5-turbo"


def query_llm_with_context(query: str, context: str):

    prompt = f"""
    Answer the user's question using ONLY the context below.

    Question:
    {query}

    Context:
    {context}
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful RAG assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content