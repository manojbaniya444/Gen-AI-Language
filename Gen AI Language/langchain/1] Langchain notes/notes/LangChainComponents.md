# Introduction
> LLms are reshaping the landscape of AI-driven product development.Among the array of tools employed for building such applications, the **LangChain** framework makes creating applications that use LLMs easy.

# What is LangChain?
LangChain is an open source toolkit available in Python and Typescript.It presents a collection of components that make constructing applications using large language models easier.This framework empowers AI developers to blend LLMS with external computation and data sources.The main objective is to let developers effortlessly infuse language processing abilities into their applications without having to build everything from the ground up.

- Working directly with complex LLMs can be intricate but LangChain furnishes a straightforward interface,streamlining the connection of LLMs with our application.

- LangChain extends the capability to couple LLMs with diverse data sources (external data like files, other applications and API data), enhancing their insights beyond their inherent general knowledge which empowers LLMs with context inherent general knowledge broadening their scope.

- LangChain empowers our LLMs to enagage with their environment, determining the subsequent actions to undertake.

# LangChain Components:
> LangChain introduces modular abstractions for essential components required to interact with language models.These components are intentionally designed to ensure simplicity in their utilization.

## Schema:
The Schema pertains to the fundamental data types and structures utilized across the codebase.

It encompasses four core components: **Text**, **ChatMessages**, **Examples** and **Documents**

## Model:
Model serve as the powerhouse of AI-driven applications.This component encompasses three distinct model types:
- Language Models
- Chat Models
- Text Embedding Models

## Prompt:
Prompt serves as an instruction for an LLM.The prompt components within LangChain assist in directing our models through text instructions.Through the utilization of prompt templates, LangChain streamlines prompt management and optimization.

## Index:
Despite LLM's extensive pre-trained knowledge base, the option to enhance contextual alignment with our specific use case is available by incorporating supplementary context within the prompt.This gap can be addressed by granting LLMs access to pertinent external data (documents or data from external sources) where indexes play a pivotal role.Indexes frequently serve as the link between documents and the model offering a simplified interface for both structured and unstructured data.

## Memory:

At its core a conversational system must have the capability to access historical messages for effective interactions.

LangChain's memory component facilitates the storage and retrieval of chat history.This component adeptly handles the storage and retrieval of conversations.**It can maintain the complete dialogue, focus on the most recent interactions, provide a summary, extract and showcase details from archived entities when mentioned or employ a tailored strategy**.

This memory component ensures that incoming questions are not processed in isolation but are cross-referenced with prior interactions.These strategies span short-term and long-term memory tailored to diverse application needs.

- Short-term memory revolves around maintaining context within a single discussion, often encompassing prio messages or their summaries.

- Long-term memory focuses on accessing and updating data across multiple chats which is where sophisticated systems like **Vector Stores** becomes essential.

Memory is vital for a consistent and relevant conversational AI experience.Short-term memory maintains context in current chats where long-term memory recalls insights from past conversations enabling deeper and personalized interactions.

## Chains:
The name LangChain is a fusion of "Lang" and "Chain" underscoring the significance of chains within the LangChain framework.

A chain serves as a comprehensive conduit seamlessly linking multiple LangChain components.

It facilitates the automatic amalgamation of various LLM calls and actions.

## Agent:
Agents utilize LLMs to select and sequence their actions.The role of an LLM is not limited to generating text:it's pivotal in informed decision-making.

[Taken from this page](https://deepchecks.com/langchain-components-a-comprehensive-beginners-guide/)