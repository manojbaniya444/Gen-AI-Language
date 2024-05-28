# Memory

Most LLM applications have a conversational interface.An essential component of a conversational is being able to refer to information introduced earlier in the conversation.At bare minimum a conversational system should be able to access some window of past messages directly.A more complex system will need to have a world model that it is constantly updating which allows it to do things like maintain information about entities and their relationships.

This ability to store information about past interactions is **Memory**.
LangChain provides a lot of utilities for adding memory to a system.These utilities can be used by themselves or incorporated seamlessly into a chain.

# Introduction

A memory system needs to support two basic actions: **reading** and **writing**.

We know that every chain defines some core execution logic that expects certain inputs.Some of these inputs come directly from the user, but some of these inputs can **come from memory**.A chain will interact with its memory system twice in a given run.

- After receiving the initial user inputs but Before executing the core logic a chain will read from its memory system and augment the user inputs.

- After executing the core logic but Before returning the answer a chain will write the inputs and outputs of the current run to memory so that they can be referred to in future runs.

![Memory Langchain](../../../images/memory.png)

# Building memory into a system

The two core design decisions in any memory system are:

- How state is stored
- How state is queried

## Storing: List of chat messages

- Underlying any memory is a history of all chat interactions.
- One of the key parts of the LangChain memory module is a series of integrations for storing these chat messages from in memory list to persistent databases.

## Querying: Data Structures and Algorithms on top of chat messages

- How the list of chat messages are stored and what data structures and algorithms are used is important
- A simple memory system might just return the most recent messages each run.
- A slightly complex memory system might return a succinct summary of the past K messages.
- A more sophisticated system might extract entities from stored messages and only return information about entities referenced in the current run.

**Each application can have different requirements for how memory is queried.**

# Getting Started

## **ConversationufferMemory** is an extremely simple form of memory that just keeps a list of chat messages in a buffer and passes those into the prompt template.

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("Hi")
memory.chat_memory.add_ai_message("Hello how may I assist you?")
```

Variables are read from memory.Empty dictionary is just a placeholder for real variables.If the memory type we are using is dependent upon the input variables we may need to pass some in.

```
memory.load_memory_variables({})
```

```
{'history: "Human: Hi\nAI: Hello how may I assist you?"}
```

## Returning memory as a string or list of messages

To return as list add return_messages=True

```python
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_user_message("Hi")
memory.chat_memory.add_ai_message("Hello how may I assist you?")
```

```
    {'history': [HumanMessage(content='Hi', additional_kwargs={}, example=False),
  AIMessage(content='Hello how may I assist you?', additional_kwargs={}, example=False)]}
```

# End to End example

```python
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

llm = OpenAI(temperature=0)

template = """You are a nice chatbot having a conversation with a human

Previous conversation:
{chat_history}

New human question: {question}
Response:"""

prompt = PromptTemplate.from_template(template)

memory = ConversationBufferMemory(memory_key="chat_history")

conversation = LLMChain(
    llm = llm,
    prompt = prompt,
    verbose = True,
    memory = memory
)
```

Here in the conversation chain we will only pass 'question' variable 'chat_history' variable will be automatically passed by the memory

```python
conversation({"question":"Hi"})
```

# Using a Chat Model

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI()

prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with a human.
        ),
        # The variable_name here is what must align with memory hai
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)

memory = ConversationBufferMemory(
    memory_key = "chat_history",
    return_messages = True
)

conversation = LLMChain(
    llm = llm,
    prompt = prompt,
    verbose = True,
    memory = memory
)

conversation({"question" : "Hi"})
```