🤖 AI Support Agent

An AI-powered customer support assistant built with LangChain, LangGraph, and Streamlit.
It can answer FAQs, handle order tracking, and simulate a real support chat experience.

🌐  [👉 Try the Live Demo](https://ai-support-agent-hyffzzbpkqcfgmsucgwqfn.streamlit.app/)

🚀 Features

✅ Answers FAQs from a JSON knowledge base

✅ Tracks order status by extracting Order IDs from queries

✅ Remembers conversation context with memory

✅ Deployable as a Streamlit web app

✅ Example of an AI Agent with tool use



📂 Project Structure
<code>
support_agent/      # Core agent logic
│── state.py        # Shared state definition
│── memory.py       # Chat memory
│── tools.py        # FAQ + order tracking tools
│── classifier.py   # Query classifier (LLM-based)
│── graph.py        # Orchestration using LangGraph
│── faqs.json       # Knowledge base
│
main.py             # CLI chat interface
app.py              # Streamlit web app
requirements.txt    # Dependencies
README.md           # Project documentation
LICENSE             # Open-source license
</code>




⚙️ Setup

Clone repo:
<code>
git clone https://github.com/YOUR_USERNAME/ai-support-agent.git
cd ai-support-agent
</code>


Install dependencies:
<code>
pip install -r requirements.txt
</code>

Create a .env file in the root:
<code>
OPENAI_API_KEY=your_api_key_here
</code>




💻 Run Locally

CLI Mode
<code>
python main.py
</code>

Web App
<code>
streamlit run app.py
</code>




🌐 Deployment

Deploy easily on Streamlit Cloud:

Push repo to GitHub

Connect Streamlit Cloud to your repo

Add OPENAI_API_KEY as a secret under project settings

You’ll get a live demo link to share (e.g., https://yourname-support-agent.streamlit.app).




📜 License

This project is licensed under the MIT License.




✅ This version has:

Shields.io badges (makes repo look legit at first glance)

Clear features list

Project structure code block

Step-by-step setup, run, and deployment instructions
