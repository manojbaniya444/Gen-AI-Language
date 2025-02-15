## Agent Architectures
Instead of hardcoding a fixed control flow of LLM application we sometimes want LLM systems that can pick its own control flow to solve more complex problems. This is the definition of an `**Agent**`. 
It is a system that uses an LLM to control the flow of application.

- LLM can route between two potential paths
- LLM can decide which of many tools to call
- LLM can decide whether the generated answer is sufficient or more work is needed to complete

## ROUTER:
- LLM can select single step from a specified set of options.
- Limited level of control

## Structured output:
- work by providing a specific format or schema that the LLM should follow in its response.

## Tool calling
- The llm can control a sequence of decisions rather than just one
- the llm can choose from and use a variety of tools to accomplish its task.

## ReAct:
A popular general purpose agent architecture that combine these expansions, integrating:
- Tool calling
- Memory
- Planning

## CUSTOM AGENT:
While routers and tool calling agents are common, customizing agent architectures often leads to better performance for specific task.

- Human in the loop
- Parallelization
- Sub-graphs
- Reflection