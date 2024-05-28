# What are LangChain Agents?
Language model that can take independent steps to fulfill instructions, langchain agents do that.They are specialized components withing the LangChain framework that act as intelligent assistants using LLMs to process natural language inout and then orchestrating a sequence of actions to achieve a desired outcome.

The core idea of agents is to use a language model to choose a sequence of actions to take.

In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.


```python
# create tool
tools = [tool1, tool2] # like search tool, retriever tool

# create the agent

# first choose the LLM we want to be guiding the agent
from langchain_openai import ChatOpenAI
llm = ChatOpenAP(model="gpt-3.5-turbo-0125", temperature=0)

# Choose the prompt we want to use to guide the agent.
prompt = ""

# Initialize the agent with LLM
from langchain.agents import create_tool_calling_agent
agent = create_tool_calling_agent(llm, tools, prompt)

# Combine the agent with the tools inside the **AgentExecutor**

from langchain.agents import AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run the agent
agent_executor.invoke({"input":"hi!"})

response_will_be = {'input': 'hi!', 'output': 'Hello! How can I assist you today?'}

# another one
agent_executor.invoke({"input":"who won the recent FIFA world cup?"})

# In this way we can operate this agent.
```

# Agent Types:
- Intended Model Type
Whether this agent is intended for Chat Models or LLMs, the main thing this affects is the prompting strategy used.We can use an agent with a different type of model than it is intended for, but it like will not product results of the same quality.

- Supports Chat History
Whether or not these agent types support chat history.If it does that means it can be used as a chatbot.If it does not then that means it's more suited for single tasks.Supporting chat history generally requires better models so earlier agent types aimed at worse models may not support it.

- Supports Multi-Input Tools
Whether or not these agent types support tools with multiple inputs.If a tool requires a single input, it is generally easier for an LLM to know how to invoke it.

- Supports Parallel Function Calling
Having an LLM call multiple tools at the same time can greatly speed up agents whether there are tasks that are assisted by doing so.However, it is much more challenging for LLMs to do this, so some agent types do not support this.

- Required Model Params
Whether this agent requires the model to support any additional parameters.Some agent types take advantage of things like OpenAI function calling,which require other model parameters.If none are required,then that means that everything is done via prompting.