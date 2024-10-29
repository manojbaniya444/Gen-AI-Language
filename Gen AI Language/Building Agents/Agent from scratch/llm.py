import requests
import json
import re
import os
from dotenv import load_dotenv
from groq import Groq

# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class Llama3:
    def __init__(self, model, system_prompt, temperature, stop=None):
        self.temperature = temperature
        self.model = model
        self.system_prompt = system_prompt
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client  = Groq(api_key=self.api_key)
        
    def generate_text(self, prompt):
        
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=self.model,
            temperature=self.temperature,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False
        )
        # TODO: Need to format here actually
        response =  chat_completion.choices[0].message.content
       
        return None 
