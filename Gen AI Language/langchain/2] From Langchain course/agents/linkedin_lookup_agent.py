from langchain_core.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url

def linkedin_lookup_agent(name: str) -> str:
    llm = ChatOpenAI(
        temperature = 0.2,
        model_name = "gpt-3.5-turbo",
    )
    
    template = """Given the full name {name} I want you to get me a link to their Linkedin Profile page. Your answer should contain only a URL."""
    
    tools_for_agent = [Tool(
        name = "Crawl Google 4 Linkedin profile page",
        func= get_profile_url,
        description="useful for when you need get the Linkedin profile page of a person from their name"
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
    
    linkedin_profile_url = agent.run(
        prompt_template.format_prompt(name = name)
    )
    
    return linkedin_profile_url 