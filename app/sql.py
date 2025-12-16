import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from pathlib import Path
import re

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()

GROQ_MODEL = os.getenv('GROQ_MODEL')

db_path = Path(__file__).parent / "resources/flipkart_products.db"


sql_prompt = """You are an expert in understanding the database schema and generating SQL queries for a natural language question asked
pertaining to the data you have. The schema is provided in the schema tags of the shoes database. 
<schema> 
table: products 

fields: 
product_link - string (hyperlink to product)	
title - string (name of the product)	
brand - string (brand of the product)	
price - integer (price of the product in Indian Rupees)	
discount - float (discount on the product. 10 percent discount is represented as 0.1, 20 percent as 0.2, and such.)	
avg_rating - float (average rating of the product. Range 0-5, 5 is the highest.)	
total_ratings - integer (total number of ratings for the product)

</schema>
Make sure whenever you try to search for the brand name, the name can be in any case. 
So, make sure to use %LIKE% to find the brand in condition. Never use "ILIKE". 
Create a single SQL query for the question provided. 
The query should have all the fields in SELECT clause (i.e. SELECT *)

Just the SQL query is needed, nothing more. Always provide the SQL in between the <SQL></SQL> tags."""

def generate_sql_query(question):
    client_sql = ChatGroq(
        model=GROQ_MODEL,
        api_key=os.environ["GROQ_API_KEY"],
        temperature=0.2,
        max_tokens=1024,
        # reasoning_format="parsed",
        timeout=None,
        max_retries=2,
        )
    
    prompt = ChatPromptTemplate([
            ("system",f'''
                {sql_prompt}
            '''),
            ("user", "Generate the SQL query for this question: {question}"),
        ])
    
     # 5. Create the Chain
    chain = prompt | client_sql
    
    answer =  chain.invoke({
        "question": question
    })
    
    return answer.content


def run_sqlite_query(query):
    if query.strip().upper().startswith('SELECT'):
        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql_query(query, conn)
            return df


# ---------- MYSQL CONFIG ----------
MYSQL_USER = "root"
MYSQL_PASSWORD = ""        # default in XAMPP
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "flipkart_db"

# ---------- CREATE ENGINE ----------
mysql_engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

def run_mysql_query(query):
    if query.strip().upper().startswith('SELECT'):
        with mysql_engine.connect() as conn:
            df = pd.read_sql_query(query, conn)
            return df   

comprehension_prompt = """You are an expert in understanding the context of the question and replying based on the data pertaining 
to the question provided. 
You will be provided with Question: and Data:. The data will be in the form of an array or a dataframe or dict. 

Reply based on only the data provided as Data for answering the question asked as Question. 
Do not write anything like 'Based on the data' or any other technical words. Just a plain simple natural language response.

The Data would always be in context to the question asked. 
For example is the question is “What is the average rating?” and data is “4.3”, 
then answer should be “The average rating for the product is 4.3”. 
So make sure the response is curated with the question and data. 
Make sure to note the column names to have some context, if needed, for your response.

There can also be cases where you are given an entire dataframe in the Data: field. 
Always remember that the data field contains the answer of the question asked. 

All you need to do is to always reply in the following format when asked about a product: 
Produt title, price in indian rupees, discount, and rating, and then product link. 
Take care that all the products are listed in list format, one line after the other. Not as a paragraph.
For example:
1. Campus Women Running Shoes: Rs. 1104 (35 percent off), Rating: 4.4 <link>
2. Campus Women Running Shoes: Rs. 1104 (35 percent off), Rating: 4.4 <link>
3. Campus Women Running Shoes: Rs. 1104 (35 percent off), Rating: 4.4 <link>

"""

def data_comprehension(question, context):
    comprehension_model = ChatGroq(
        model=GROQ_MODEL,
        api_key=os.environ["GROQ_API_KEY"],
        temperature=0.2,
        # max_tokens=1024,
        # reasoning_format="parsed",
        timeout=None,
        max_retries=2,
        )
    
    prompt = ChatPromptTemplate([
            ("system",f'''
                {comprehension_prompt}
            '''),
            ("user", "QUESTION: {question}. DATA: {context}"),
        ])
    
     # 5. Create the Chain
    chain = prompt | comprehension_model
    
    answer =  chain.invoke({
        "question": question,
        "context": context
    })
    
    return answer.content

def sql_chain(question):
    sql_query = generate_sql_query(question)
    pattern = "<SQL>(.*?)</SQL>"
    matches = re.findall(pattern, sql_query, re.DOTALL)

    if len(matches) == 0:
        return "Sorry, LLM is not able to generate a query for your question"

    print(matches[0].strip())
    print("*********************************")
    
    response = run_sqlite_query(matches[0].strip())
    if response is None:
        return "Sorry, there was a problem executing SQL query"
    print(response)
    print("*********************************")
    
    context = response.to_dict(orient='records')

    answer = data_comprehension(question, context)
    return answer
        
if __name__ == "__main__":
    # sample_query = "SELECT * FROM products LIMIT 5;"
    # sample_query = "SELECT DISTINCT brand FROM products LIMIT 20;"
    # sample_query = "SELECT * FROM products WHERE LOWER(brand) LIKE '%%nike%%';"
    # result_df = run_sqlite_query(sample_query)
    # print(result_df)
    # print("------------------------")
    # result_df = run_mysql_query(sample_query)
    # print(result_df)
    
    # question = "All shoes with rating higher than 4.5 and total number of reviews greater than 500"
    # # question = "Show top 3 shoes in descending order of rating"
    # # question = "Show me 3 running shoes for woman"
    # # question = "sfsdfsddsfsf
    # sql_query = generate_sql_query(question)
    # print(sql_query)

    question = "PUMA shoes with rating higher than 4.5 and show descending order with respect to price"
    answer = sql_chain(question)
    print(answer)
    