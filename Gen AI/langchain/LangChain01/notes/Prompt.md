# Prompts:

A prompt for a language model is a set of instructions or input provided by a user to guide the model's response helping it understand the context and generate relevant and coherent language-based output.

A template may include instructions, few-shot examples and specific context and questions appropriate for a given task.

LangChain provides a tooling to create and work with prompt templates.

## PromptTemplate

```python
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
prompt_template.format(adjective="funny", context="chickens")
```

```
"Tell me a funny joke about chickens"
```

The template supports any number of variables, including no variables

```python
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me a joke")
prompt_template.format()
```

```
"Tell me a joke"
```

## ChatPromptTemplate

The prompt to chat models is a list of chat messages.

Each chat message is associated with content, and an additional parameter called **role**.
For example in the OpenAI Chat Completion API, a chat message can be associated with an **AI assistant**, **a human** or a **system** role.

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai","I am doing well, thanks!"),
        ("human","{user_input}"),
    ]
)

messages = chat_template.format_messages(name="Bob", user_input="What is yout name?")
```
