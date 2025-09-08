from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = PromptTemplate.from_template("""
You are a query classifier. 
Classify the user query into one of: [FAQ, ORDER, GENERAL].
Query: {query}
Class:
""")

def classify_query(query: str) -> str:
    result = llm.invoke(prompt.format(query=query))
    return result.content.strip().upper()
