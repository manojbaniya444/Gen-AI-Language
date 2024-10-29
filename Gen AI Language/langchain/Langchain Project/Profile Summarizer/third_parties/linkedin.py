# connecting application to linked in
import requests
import os

def scrape_linkedin_profile(linkedin_profile_url):
    """scrape information from linkedin profiles,
    manually scrape the information from the Linkedin profile."""

    # 1. scrape directly
    
    # 2. get the same response using the gist.github.response
    
    response = requests.get(
        url = linkedin_profile_url
    )
    
    return response