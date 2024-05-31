from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
from agents.linkedin_lookup_agent import linkedin_lookup_agent
from agents.twitter_lookup_agent import twitter_lookup_agent
from output_parser import person_intel_parser, PersonIntel

load_dotenv()

information = """Hi my name is john doe. I am 25 years old and I am a software engineer. I completed my Computer Science course from Stanford University and then i got internship at Google right after my university. Now I am working as a full time software engineer at Perplexity AI."""

def get_summary(name: str) -> PersonIntel:
    linkedin_url_profile = linkedin_lookup_agent(name = "Manoj Kumar Baniya")
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url = linkedin_url_profile)
    
    twitter_username = twitter_lookup_agent(name = "Manoj Kumar Baniya")
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=90)
    
    summary_template = """Given the linkedin information {linkedin_information} and twitter information {twitter_information} about a person from I want you to create:
    1. a short summary
    2. Interesting facts about them
    3. A topic that may interest them
    4. 2 creative Ice breakers to open a conversation with them\n{format_instruction}
    """
    
    summary_prompt_template = PromptTemplate(input_variables = ["linkedin_information", "twitter_information"], template = summary_template, partial_variables={"format_instruction": person_intel_parser.get_format_instruction()})
    
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
    # TODO: llm chain is depriciated now use llm chains runnables 
    # TODO: add the information from respective linkedin and twitter agents response here
    response = chain.invoke(input = [{"linkedin_information": information,
                                      "twitter_information": information}])
    
    # return response["text"]
    return person_intel_parser.parse(response["text"])

if __name__ == "__main__":
    print("Hello from the langchain.")
    
    response = get_summary(name = "Manoj Kumar Baniya")