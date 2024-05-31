from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()

information = """Hi my name is john doe. I am 25 years old and I am a software engineer. I completed my Computer Science course from Stanford University and then i got internship at Google right after my university. Now I am working as a full time software engineer at Perplexity AI."""

if __name__ == "__main__":
    print("Hello from the langchain.")
    
    summary_template = """Given the information {information} about a person from I want you to create:
    1. a short summary
    2. Interesting facts about them
    """
    
    summary_prompt_template = PromptTemplate(input_variables = ["information"], template = summary_template)
    
    # # TODO: api key
    llm = CTransformers(
        model = "../../local LLM/llama2-7b-q2chat.bin",
        model_type = "llama",
        max_new_tokens = 900,
        temperature = 0.2
    )
    
    chain = LLMChain(llm = llm, prompt = summary_prompt_template)
    
    # response = chain.run(information = information)
    url = os.environ["API_ENDPOINT_PROFILE"]
    
    # give the response from the api json in the chain
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url = url)
    
    # give the response from the api json in the chain
    # TODO: llm chain is depriciated now use llm chains runnables
    response = chain.invoke(input = [{"information": information}])
    
    print(response["text"])