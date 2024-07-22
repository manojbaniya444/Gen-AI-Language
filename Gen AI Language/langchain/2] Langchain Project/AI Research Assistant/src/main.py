from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import requests
from bs4 import BeautifulSoup

template = """"
Summarize the following question based on the context:

Question: {question}

Context:

{context}
"""

prompt = ChatPromptTemplate.from_template(template=template)

def scrape_text(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.txt, "html.parser")
            page_text = soup.get_text(separator=" ", strip=True)
            return page_text
        else:
            return f"Failed to retrieve the webpage: Status code {response.status_code}"
    except Exception as e:
        print(e)
        return f"Failed to retrieve the webpage: {e}"

url="https://www.gitselect.com/post/what-is-langchain-langsmith-and-langserve#:~:text=LangSmith%20and%20LangServe%20are%20integral,of%20your%20LLM%2Dpowered%20applications."