import { ChatGroq } from "@langchain/groq";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { StringOutputParser } from "@langchain/core/output_parsers";
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

const prompt = ChatPromptTemplate.fromMessages([
  ["system", "Generate the joke on topic mentioned by the user."],
  ["human", "{topic}"],
]);

const parser = new StringOutputParser();

const modelChain = prompt.pipe(model).pipe(parser);

const response = await modelChain.invoke({
  topic: "chicken",
});

console.log(response);
