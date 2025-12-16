from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os
load_dotenv()


def talk(query):
    client_smalltalk = ChatGroq(
        model=os.environ['GROQ_MODEL'],
        api_key=os.environ["GROQ_API_KEY"],
        temperature=0.7,
        max_tokens=512,
        timeout=None,
        max_retries=2,
    )

    prompt = ChatPromptTemplate([
            ("system",'''
                You are a helpful and friendly chatbot designed for small talk. You can answer questions about the weather, your name, your purpose, and more.
            '''),
            ("user", "QUESTION: {query}"),
        ])
    
     # 5. Create the Chain
    chain = prompt | client_smalltalk
    
    answer =  chain.invoke({
        "query": query
    })
    
    return answer.content