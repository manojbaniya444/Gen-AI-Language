from langchain_core.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url

def twitter_lookup_agent(name: str) -> str:
    llm = ChatOpenAI(
        temperature = 0.2,
        model_name = "gpt-3.5-turbo",
    )
    
    template = """Given the full name {name} I want you to get me a link to their Twitter Profile page. Extract username. In your answer only give the username."""
    
    tools_for_agent = [Tool(
        name = "Crawl Google 4 Twitter profile page",
        func= get_profile_url,
        description="useful for when you need get the Twitter page URL."
    )]
    
    agent = initialize_agent(
        tools = tools_for_agent,
        llm = llm,
        agent = AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose = True 
    )
    
    prompt_template = PromptTemplate(
        template = template,
        input_variables = ["name"]
    )
    
    twitter_username = agent.run(
        prompt_template.format_prompt(name = name)
    )
    
    return twitter_username 