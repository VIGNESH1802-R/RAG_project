# from embedder import embed_user_query
# from vectorstore import search_in_pinecone
# from llm import query_llm_with_context

# def process_user_query(query: str):

# # embed the user's query to create a vector representation

#     query_vector = embed_user_query(query)

# # search the vector db to find top matching chunks related to the user's question
#     matched_chunks = search_in_pinecone(query_vector)

# # send the user query and the search result (query + context) to the llm for generating respomnse
#     # generated_response = query_llm_with_context(query,matched_chunks)
#     # print(generated_response)


#     context = "\n\n".join(matched_chunks)

# generated_response = query_llm_with_context(
#     query,
#     matched_chunks
# )

# print("\nAnswer:\n")
# print(generated_response)



# # if __name__ == "__main__":
# #     user_query = "what is the work timing policy?"
# #     process_user_query(user_query)


# if __name__ == "__main__":

#     while True:

#         user_query = input("\nAsk your question: ")

#         if user_query.lower() == "exit":
#             break

#         process_user_query(query)



from embedder import embed_user_query
from vectorstore import search_in_pinecone
from llm import query_llm_with_context

def process_user_query(query: str):

    # Convert question into embedding
    query_vector = embed_user_query(query)

    # Search similar chunks in Pinecone
    matched_chunks = search_in_pinecone(query_vector)

    # Generate final answer using LLM
    generated_response = query_llm_with_context(
        query,
        matched_chunks
    )

    print("\nANSWER:\n")
    return generated_response


if __name__ == "__main__":

    while True:

        query = input("\nAsk your question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        process_user_query(query)


