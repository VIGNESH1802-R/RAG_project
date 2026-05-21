from pdfreader import read_pdf
from chunker import chunk_pages
from embedder import embed_chunks
from vectorstore import store_in_pinecone
from typing import List

pdf_path ="./resourses/history book.pdf"

def run():
    # extract text
    pages = read_pdf(pdf_path)

    # # chunk the data into smaller pieces
    # chunks = chunk_pages(pages)

    # # embed the chunks using openAI's embedding model
    # embeddings = embed_chunks(chunks)

    # #store hte chunks and their embeddings in pinecone vectore database  
    # store_in_pinecone(chunks, embeddings)

    chunks = chunk_pages(pages, chunk_size=900, chunk_overlap=150)

    embedded_chunks = embed_chunks(chunks)

    store_in_pinecone(chunks, embedded_chunks, namespace="")
    

if __name__ == "__main__":
    run()
