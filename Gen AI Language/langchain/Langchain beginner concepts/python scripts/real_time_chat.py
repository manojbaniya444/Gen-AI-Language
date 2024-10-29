# importing the required libraries
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

# loading the environment variables
load_dotenv()

# setting up the groq API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# load the model
model = ChatGroq(model="llama3-8b-8192")

# setting up the system message
system_message = SystemMessage(
    content="You are a helpful AI assistant who will answer only questions related to Artificial Intelligence and nothing else. If asked about anything else, you will apologize with different utterences politely and ask the user to ask questions related to AI only. Remember, if asked about yourself you will answer that you are created by Manoj and also keep the conversation short and simple and the response with maximum of 5 lines.",
)

# creating a chat history list
chat_history = []
chat_history.append(system_message)

print("___________________CHAT____________________________\n")

# Chat loop
while True:
    # getting the user input
    user_query = input("You: ")
    if user_query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=user_query))
    
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    
    # remove the first element if the length of the chat history is greater than 5
    if len(chat_history) > 5:
        chat_history.pop(0)
    print(f"AI: {response}")
    print("\n")