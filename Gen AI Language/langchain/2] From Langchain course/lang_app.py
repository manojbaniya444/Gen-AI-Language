from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

information = """Hi my name is john doe. I am 25 years old and I am a software engineer. I completed my Computer Science course from Stanford University and then i got internship at Google right after my university. Now I am working as a full time software engineer at Perplexity AI."""

if __name__ == "__main__":
    print("Hello from the langchain.")
    
    # summary_template = """given the information about a person from I want to you to create:
    
    # information: {information}

    # 1. a short summary
    # 2. two interesting facts about them
    # """
    
    # summary_prompt_template = PromptTemplate(input_variables = ["information"], template = summary_template)
    
    # # TODO: api key
    # llm = ChatOpenAI(temperature = 0, model_name="gpt-3.5-turbo")
    
    # chain = LLMChain(llm = llm, prompt = summary_prompt_template)
    
    # response = chain.run(information = information)
    url = os.environ["API_ENDPOINT_PROFILE"]
    
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url = url)
    
    print(linkedin_data.json())