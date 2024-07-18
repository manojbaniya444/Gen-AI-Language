import json

# Your content string, wrapped in curly braces and cleaned up
text = '{"tool_choice": "basic_calculator", "tool_input": "{\\"num1\\": 2, \\"num2\\": 2, \\"operation\\": \\"add\\"}"}'

# Load the outer JSON
data = json.loads(text)

# If needed, parse the nested JSON inside 'tool_input'
data['tool_input'] = json.loads(data['tool_input'])

# Print the result
print(data)
