import streamlit as st
from router import router
from faq import faq_query_answer
from sql import sql_chain
from smalltalk import talk

st.title("E-commerce FAQ Chatbot")

query = st.chat_input("Write your question here...")

def ask(query):
    route = router(query).name
    if route == 'faq':
        
        answer = faq_query_answer(query)
        return answer
    elif route == 'sql':
        answer = sql_chain(query)
        return answer
    
    elif route == 'small-talk':
        answer = talk(query)
        return answer
    else:
        return f"Sorry, {route} related queries are not handled yet."


if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query:
    with st.chat_message("user"):
        st.markdown(query)  
    st.session_state.messages.append({"role": "user", "content": query})
        
    response = ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})