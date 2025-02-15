# TODO: make module of each class and function

from termcolor import colored
from prompts import agent_system_prompt_template
from llm import Llama3
from toolbox import ToolBox
from basic_calculator import basic_calculator
from reverser import reverse_string

class Agent:
    def __init__(self, tools, model_service, model_name, stop=None):
        """
        Initializes the agent with a list of tools and a model.
        
        Parameters:
        tools (list): List of tool functions.
        model_service (str): The model service class with a generate_text method.
        model_name (str): The name of the model to use.
        """
        
        self.tools = tools
        self.model_service = model_service
        self.model_name = model_name
        self.stop = stop
        
    def prepare_tools(self):
        """
        Stores the tools in the toolbox and returns their descriptions.
        
        Returns:
        str: Description of the tools stored in the toolbox.
        """
        
        toolbox = ToolBox()
        toolbox.store(self.tools)
        tool_description = toolbox.tools()
        return tool_description
    
    def think(self, prompt):
        """
        Runs the generate_text method on the model using the systemprompt template and tool descriptions.
        
        Parameters:
        prompt (str): The user query to generate a response for.
        
        Returns:
        dict: The response from the model as a dictionary.
        """
        
        tool_description = self.prepare_tools()
        agent_system_prompt = agent_system_prompt_template.format(tool_description=tool_description)
        
        # create an instance of the model service with the system prompt
        
        # does llm need stop token or not?
        model_instance = self.model_service(
            model=self.model_name,
            system_prompt=agent_system_prompt,
            temperature=0.5,
            stop=self.stop
        )
        
        # generate and return the response dictionary
        # TODO: Not getting the dict 
        agent_response_dict = model_instance.generate_text(prompt)
        print("HEHE: ", agent_response_dict)
        return agent_response_dict
    
    def work(self, prompt):
        """
        Parses the dictionary returned from think and executes the appropriate tool.
        
        Parameters:
        prompt (str): The user query to generate a response for.
        
        Returns:
        The response from executing the appropriate tool or the tool_input if no matching tool is found.
        """
        
        # TODO: Here get the correct formated response from the model
        agent_response_dict = self.think(prompt)
        # tool_choice = agent_response_dict.get("tool_choice")
        # tool_input = agent_response_dict.get("tool_input")
        tool_choice = "reverse_string"
        tool_input = "encyclopedia"
        
        
        for tool in self.tools:
            if tool.__name__ == tool_choice:
                response = tool(tool_input)
                
                print(colored(f"\n\nResponse from the tool: {response}", "green"))
                return
            
        print(colored(tool_input, "cyan"))
        
        return
    
    
if __name__ == "__main__":
    tools = [basic_calculator, reverse_string]
    model_service = Llama3
    model_name = "llama3-8b-8192"
    
    agent = Agent(tools=tools, model_service=model_service, model_name=model_name, stop = None)
    
    while True:
        prompt = input("User Query: ")
        if prompt.lower() == "exit":
            break
        
        agent.work(prompt)