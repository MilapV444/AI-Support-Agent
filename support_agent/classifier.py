from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = PromptTemplate.from_template("""
You are a query classifier. 
Classify the user query into one of: [FAQ, ORDER, GENERAL].
Query: {query}
Class:
""")

chain = prompt | llm

def classify_query(query: str) -> str:
    result = chain.invoke({"query": query})
    return result.content.strip().upper()
