import { ChatGroq } from "@langchain/groq";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import * as dotenv from "dotenv";

dotenv.config();

// defining model constant
const models = {
  llama38b: "llama3-8b-8192",
};

// model
const model = new ChatGroq({
  model: models.llama38b,
  apiKey: process.env.API_KEY,
  temperature: 0.5,
});

// prompt
const prompt = ChatPromptTemplate.fromTemplate(
  "You will say 3 jokes about {topic}"
);

// prompt from messages
const prompt2 = ChatPromptTemplate.fromMessages([
  [
    "system",
    "Generate a joke about the topic mentioned below in hinglish language.",
  ],
  ["human", "{topic}"],
]);

// we can also format prompt
const formatted_prompt = await prompt.format({
  topic: "chickens",
});

// creating chain
const modelChain = prompt.pipe(model);

// invoking model
// const response = await modelChain.invoke({
//   topic: "dog",
// });

const modelChain2 = prompt2.pipe(model);

const response = await modelChain2.invoke({
  topic: "dog",
});

// logging the response content
console.log(response?.content);
