import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ["LINKEDIN_SCRAPE_API_KEY"]

headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/manoj-baniya-747683265/',

}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)
