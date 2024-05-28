# What is LangChain ?
LangChain is a framework for developing applications powered by Large Language Models (LLMs).As a languag model integration framework, LangChain's use-cases largerly overlap with those of language models in general, including docment analysis and summarization, chatbots and code analysis.

Langchain simplifies every stage of the LLM application lifecycle:

- **Development**: Building applications using LangChain's Open Source building blocks and components.

- **Productionization**: Using **LangSmith** to inspect, monitor and evaluate chains so that we can continuously optimize and deplo with confidence.

- **Deployment**: Turn any chain into an API with LangServe.

# Use cases
- Question answering with RAG
- Extracting structured output
- Chatbots
- many more

## Example: Desiging a chatbot

### Overview
Chatbots are one of the most popular use cases for LLMs.The core features of chatbots are that they can have long-running stateful conversations and can answer user question using relevant information.

### Architectures
Designing a chatbot involves considering various techniques with different benefits and tradeoffs depending on what sorts of question we expect it to handle.

For example: chatbots commonly use **Retrieval Augmented Generation (RAG)** over private data to better answer domain-specific  questions. 

--- 
We also might choose to route between multiple data sources to ensure it only uses the most topical context for final question answering, or choose to use a more specialized type of chat history or memory than just passing messages back and forth.

![chat-bot](../images/chatbot.png)

[read more about this](https://python.langchain.com/v0.1/docs/use_cases/chatbots/)

---

# Ecosystem
## LangSmith 💎
Trace and evaluate language model applications and intelligent agents to help move from prototype to production.

## LangGraph 💎
Build statefil, multi-actor applications with LLMs.

## LangServe 💎
Deploy LangChain runnables and chains as REST APIs