# LangGraph Agent: Local LLM Workflow with Ollama

This project demonstrates how to use LangGraph and LangChain to build an agent-like workflow powered by a local LLM using [Ollama](https://ollama.com/). It's lightweight, fully offline, and great for experimenting with multi-step reasoning.

## 🚀 Features

- LangGraph agent flow using LangChain tools
- Mistral/Phi3 models running locally via Ollama
- CPU-only friendly (for systems without powerful GPUs)
- Easy integration and fast iteration using Python

## 🧠 Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/download) installed
- Models pulled (e.g., `mistral`, `phi3`, `llama3`)
- `langchain`, `langgraph`, `langchain-community` Python libraries

## 📦 Installation

```bash
# Create a virtual environment
python -m venv lngraph
cd lngraph
.\Scripts\activate  # or source bin/activate on Linux/Mac

# Install dependencies
pip install langchain langgraph langchain-community


## 🧪 Running the Agent 
# Run Ollama in another terminal (if not running)
ollama run phi3

# Run your agent script
python main.py

## 🤝 Contributing

Contributions, issues, and suggestions are welcome!

If you'd like to contribute, please fork the repo and create a pull request with your changes. If you're not sure where to start, open an issue and let's talk.

```bash
# Fork the repository
# Clone your fork
git clone https://github.com/your-username/LangGraph_AGENT_01.git

# Create a branch for your feature/fix
git checkout -b feature-name

# Make your changes and commit
git add .
git commit -m "Add: your change description"

# Push and create a pull request
git push origin feature-name
