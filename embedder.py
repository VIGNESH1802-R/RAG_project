# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# from typing import List

# # load environment variables from .env file
# load_dotenv()

# # Initialize OpenAI client
# client = OpenAI(api_key="AIzaSyCr66WGD8DdV6H3p76V6S1dzVGBs-3fHYg")
# EMBEDDING_MODEL = "text-embedding-3-small"  # 1536-dimension vectors

# def embed_chunks(chunks: List[str]) -> List[List[float]]:
#     """Embeds chunks using OpenAI's embedding model."""
#     embeddings = []
#     for chunk in chunks:
#         response = client.embeddings.create(
#             input=chunk,
#             model=EMBEDDING_MODEL
#         )
#         embeddings.append(response.data[0].embedding)
    

#     return embeddings

# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(
#     api_key="AIzaSyD3rUs_k5RuCcFL3AdttryZfK2DmV8QNRM"
# )

# EMBEDDING_MODEL = "gemini-embedding-001"


# def embed_chunks(chunks):

#     embedded_chunks = []

#     for chunk in chunks:

#         # print("Embedding chunk...")

#         # response = client.models.embed_content(
#         #     model=EMBEDDING_MODEL,
#         #     contents=chunk
#         # )


#         response = client.embeddings.create(
#     input=query,
#     model=EMBEDDING_MODEL
# )

#     return response.data[0].embedding

#         # embedded_chunks.append(
#         #     response.embeddings[0].values
#         # )

#     return embedded_chunks

# # def embed_user_query(query: str) -> List[float]:
# #     """Embeds a user query using OpenAI's embedding model."""
# #     response = client.embeddings.create(
# #         input=query,
# #         model=EMBEDDING_MODEL
# #     )


# def embed_user_query(query: str):

#     response = client.models.embed_content(
#         model=EMBEDDING_MODEL,
#         contents=query
#     )

#     return response.embeddings[0].values


#     # return response.data[0].embedding


# # from google import genai
# from dotenv import load_dotenv
# from typing import List
# import os
# from openai import OpenAI

# load_dotenv()

# client = openai.Client(
#     api_key="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"
# )

# EMBEDDING_MODEL = "gemini-embedding-001"


# # Embed PDF chunks
# def embed_chunks(chunks: List[str]) -> List[List[float]]:

#     embedded_chunks = []

#     for chunk in chunks:

#         response = client.models.embed_content(
#             model=EMBEDDING_MODEL,
#             contents=chunk
#         )

#         embedded_chunks.append(
#             response.embeddings[0].values
#         )

#     return embedded_chunks


# # Embed user query
# def embed_user_query(query: str) -> List[float]:

#     response = client.models.embed_content(
#         model=EMBEDDING_MODEL,
#         contents=query
#     )

#     return response.embeddings[0].values


from openai import OpenAI
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()

client = OpenAI(
    api_key="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")


EMBEDDING_MODEL = "text-embedding-3-small"


# Embed PDF chunks
def embed_chunks(chunks: List[str]) -> List[List[float]]:

    embedded_chunks = []

    for chunk in chunks:

        response = client.embeddings.create(
            input=chunk,
            model=EMBEDDING_MODEL
        )

        embedded_chunks.append(
            response.data[0].embedding
        )

    return embedded_chunks


# Embed user query
def embed_user_query(query: str) -> List[float]:

    response = client.embeddings.create(
        input=query,
        model=EMBEDDING_MODEL
    )

    return response.data[0].embedding