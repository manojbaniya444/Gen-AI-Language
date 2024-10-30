# Prompt Engineering

Developing and Optimizing prompts to efficiently use **Large Language Models** for a wide variety of application. Prompt Engineering helps to better understand the capability of LLM.

The approach of designing effective prompts to instruct the model to perform a desired task is called `**Prompt Engineering**`.

# LLM Setting

We can configure a few parameter to get different result for our prompting.

- **Temperature** : Higher the temperature, more randomness in the next token, lower the temperature more fix the next token. So when we want our model to be creative and select token after increasing the probability of other token we can change the temperature value in the API setting.

- **Top P** : A sampling technique with temperature called `nucleus sampling`. If we are looking for more diverse response increase it.Top P means only the tokens comprising the top_p probability are considered for response.

- Alter **top_p** or **temperature** but not both.

- **Max Length** : number of tokens the model should generate.`

- **Stop Sequence** : string that stop response.

- **Frequence Penalty** : penalty on token that appear again and again.

# Prompting

We can structure our prompt using three different role:

- **system** : set the overall behaviour of the assistant.
- **assistant** : model response.
- **user** : our prompt

# Elements of a Prompt

- Instruction
- Context
- Input Data
- Output Indicator (how we want)

```javascript
let prompt = `
Classify the text into neutral, negative or positive

Text: I think the movie was good.

Sentiment:
`;

response = model(prompt); // positive
```

# Designing Prompt

- Keep it simple
- Experiment what work best
- Provide clear instruction like `**summarize**`, `**translate**`, `**classify**`, ...

```javascript
prompt = `
### Instruction###
Translate the text below to Nepali:
Text: "what is LLM?"
`;
model(prompt);
```

- Specificity
Be very specific about the instruction and task that we want.

- Avoid saying what not to do but say what to do.

# Prompting Technique

- [Zero shot and Few shot prompting](./zero_shot_few_shot_prompting.ipynb)