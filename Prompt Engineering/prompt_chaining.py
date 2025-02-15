import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

model_name = "llama3-8b-8192"

from groq import Groq

client = Groq(api_key=api_key)

document = """
Antarctica is Earth's southernmost continent. It contains the geographic South Pole and is situated in the Antarctic region of the Southern Hemisphere. It is the fifth-largest continent and is covered by an ice sheet, which contains about 60% of the world's fresh water. Despite its harsh climate, Antarctica is home to a variety of wildlife, including penguins, seals, and various types of birds.
"""

prompt1 = """
Given the document below extract the facts in <quote> tag.
If no fact is found, return "No fact found".

## document ##
{context}
## document ##
"""

prompt1 = prompt1.format(context=document)

prompt2 = """
Given the facts in <quote> describe briefly about each fact.
If no fact, return "No fact found".

## fact ##
{context}
## fact ##
"""

response1 = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": prompt1
        }
    ],
    model = model_name
)

facts = response1.choices[0].message.content

response2 = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": prompt2.format(context=facts)
        }
    ],
    model = model_name
)

answer = response2.choices[0].message.content

print(answer)