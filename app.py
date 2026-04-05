from fastapi import FastAPI
from pydantic import BaseModel
from support_agent.graph import build_graph

app = FastAPI()

graph = build_graph()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "AI Support Agent API is running"}

@app.post("/chat")
def chat(request: QueryRequest):
    print("Received query:", request.query)  # 👈 ADD THIS

    try:
        result = graph.invoke({
            "query": request.query,
            "response": ""
        })
        print("Response:", result["response"])  # 👈 ADD THIS
        return {"response": result["response"]}
    
    except Exception as e:
        print("ERROR:", str(e))  # 👈 IMPORTANT
        return {"response": f"Error: {str(e)}"}
