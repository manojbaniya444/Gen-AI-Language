from langchain.serpapi import SerpAPIWrapper

def get_profile_url(text: str) -> str:
    """searches for linkedin profile page
    
    parameters:
    text: str: the text to search for
    
    returns:
    str: the linkedin profile page url
    """
    
    # we are using google serp API for searching
    # TODO: not returning the url fix it and also give the apikey
    search = SerpAPIWrapper()
    
    result = search.run(f"{text}")
    
    return result