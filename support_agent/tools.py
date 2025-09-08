import json
import os

def load_faqs():
    file_path = os.path.join(os.path.dirname(__file__), "faqs.json")
    with open(file_path, "r") as f:
        return json.load(f)

FAQS = load_faqs()

def faq_tool(query: str) -> str:
    for q, a in FAQS.items():
        if q.lower() in query.lower():
            return a
    return None

def order_tracking_tool(query: str) -> str:
    order_id = ''.join([c for c in query if c.isdigit()])
    if order_id:
        return f"Order {order_id} has been shipped and will arrive tomorrow."
    return "I couldn’t find an order ID in your query."
