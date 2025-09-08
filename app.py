import streamlit as st
from support_agent.graph import build_graph

st.set_page_config(page_title="AI Support Agent", page_icon="🤖")

st.title("🤖 AI Support Agent")
st.write("Ask me about orders, shipping, or support.")

if "graph" not in st.session_state:
    st.session_state.graph = build_graph()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Customer:", "")

if st.button("Send") and query:
    result = st.session_state.graph.invoke({"query": query, "response": ""})
    st.session_state.chat_history.append(("Customer", query))
    st.session_state.chat_history.append(("Support Agent", result["response"]))

for speaker, text in st.session_state.chat_history:
    st.write(f"**{speaker}:** {text}")
