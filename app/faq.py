from pathlib import Path
import pandas as pd
from langchain_chroma import Chroma
from langchain_core.documents import Document
from chromadb.utils import embedding_functions
import chromadb
from langchain_core.embeddings import Embeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os
load_dotenv()

# Wrapper for Chroma embeddings → LangChain Embeddings
class ChromaEmbeddingWrapper(Embeddings):
    def __init__(self, chroma_embed_fn):
        self.embed_fn = chroma_embed_fn

    def embed_documents(self, texts):
        return self.embed_fn(texts)

    def embed_query(self, text):
        return self.embed_fn([text])[0]

faq_paths = Path(__file__).parent / "resources/faq_data.csv"

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name='sentence-transformers/all-MiniLM-L6-v2'
        )


wraper_embedding = ChromaEmbeddingWrapper(ef)

collection_name_faq = 'faqs'

# Create IN-MEMORY Chroma client
chroma_client = chromadb.Client() 

def ingest_faq_data(path):
    # Check if the collection exists
    existing_collections = chroma_client.list_collections()
    if collection_name_faq not in [c.name for c in existing_collections]:
        print("Ingesting FAQ data into Chromadb...")
    
        # Load FAQ CSV
        df = pd.read_csv(path)
        
        # Convert each row into a LangChain "Document"
        documents = []
        for idx, row in df.iterrows():
            doc = Document(
                page_content=row["question"],   # content to embed
                metadata={"answer": row["answer"], "id": f"id_{idx}"},
            )
            documents.append(doc)
        
         # Create the Chroma  (collection) and insert data
        Chroma.from_documents(
            documents=documents,
            embedding=wraper_embedding,
            collection_name=collection_name_faq,
            client=chroma_client                # <-- use in-memory client
        )

        print(f"FAQ Data successfully ingested into Chroma collection: {collection_name_faq}")

    else:
        print(f"Collection {collection_name_faq} already exists")

def get_relevant_qa(query):
    vectordb = Chroma(
        collection_name=collection_name_faq,
        embedding_function=wraper_embedding,
        client=chroma_client                # <-- same in-memory client
    )

    return vectordb.similarity_search_with_score(query, k=2)

def generate_answer(query, context):
    # 3. Initialize Groq LLM
    groq_llm = ChatGroq(
        model=os.environ['GROQ_MODEL'],
        api_key=os.environ["GROQ_API_KEY"],
        temperature=0,
        max_tokens=None,
        # reasoning_format="parsed",
        timeout=None,
        max_retries=2,
    )
    
    # 4. Create the prompt
    prompt = ChatPromptTemplate([
            ("system", '''
                Given the following context and question, generate answer based on this context only.
                If the answer is not found in the context, kindly state "I don't know". Don't try to make up an answer.
    
                CONTEXT: {context}
            '''),
            ("user", "Answer this question: {query}")
        ])
    
    # 5. Create the Chain
    chain = prompt | groq_llm
    
    answer =  chain.invoke({
        "context": context,
        "query": query
    })
    
    return answer
    

def faq_chain(query):
     # 1. Retrieve top-k relevant FAQ documents
    result = get_relevant_qa(query)
    
     # 2. Build context from retrieved answers
    context = " ".join([doc.metadata["answer"] for doc, score in result])
    print("Context:", context)
    
    # 3. Generate the Answer
    answer = generate_answer(query, context)
    return answer.content
    
def faq_query_answer(query):
    ingest_faq_data(faq_paths)
    answers = faq_chain(query)
    return answers


if __name__ == "__main__":
    # print(faq_paths)
    ingest_faq_data(faq_paths)
    query = "what's your policy on defective products?"
    query = "Do you take cash as a payment option?"
    # result = get_relevant_qa(query)
    answers = faq_chain(query)
    print(answers)