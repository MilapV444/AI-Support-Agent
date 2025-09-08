from support_agent.graph import build_graph

def run_cli():
    graph = build_graph()
    print("AI Support Agent (type 'exit' to quit)\n")
    while True:
        query = input("Customer: ")
        if query.lower() == "exit":
            break
        result = graph.invoke({"query": query, "response": ""})
        print("Support Agent:", result["response"])

if __name__ == "__main__":
    run_cli()
