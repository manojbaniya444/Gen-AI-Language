import { ChatGroq } from "@langchain/groq";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { CommaSeparatedListOutputParser } from "@langchain/core/output_parsers";
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

async function listOutputParserHandler() {
  const prompt = ChatPromptTemplate.fromTemplate(
    "Provide a 5 synonym from the word {word} speratated by comma."
  );

  const outputParser = new CommaSeparatedListOutputParser();

  const modelChain = prompt.pipe(model).pipe(outputParser);

  const response = await modelChain.invoke({
    word: "happy",
  });

  return response;
}

const response = await listOutputParserHandler();
console.log(response);
