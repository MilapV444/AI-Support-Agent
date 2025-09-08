from langgraph.graph import StateGraph, END
from support_agent.state import AgentState
from support_agent.classifier import classify_query
from support_agent.tools import faq_tool, order_tracking_tool

def route_query(state: AgentState) -> str:
    query = state["query"]
    category = classify_query(query)

    if category == "FAQ":
        answer = faq_tool(query)
        return {"query": query, "response": answer or "Sorry, I don’t have an answer for that."}
    elif category == "ORDER":
        return {"query": query, "response": order_tracking_tool(query)}
    else:
        return {"query": query, "response": "Sorry, I don’t have an answer for that."}

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("router", route_query)
    graph.set_entry_point("router")
    graph.set_finish_point("router")
    return graph.compile()
