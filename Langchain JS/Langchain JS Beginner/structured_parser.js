import { ChatGroq } from "@langchain/groq";
import { ChatPromptTemplate } from "@langchain/core/prompts";

import { StructuredOutputParser } from "langchain/output_parsers";

import * as dotenv from "dotenv";

dotenv.config();

const models = {
  llama38b: "llama3-8b-8192",
  llama370b: "llama3-70b-8192",
};

const model = new ChatGroq({
  model: models.llama38b,
  apiKey: process.env.API_KEY,
});

const parser = StructuredOutputParser.fromNamesAndDescriptions({
  name: "The name of the person",
  age: "The age of the person",
});

const prompt = ChatPromptTemplate.fromTemplate(
  `Extract information from the following phrase: {phrase} in json format.

    Formatting instructions: {format_instructions}
    `
);

// console.log(parser.getFormatInstructions());

const instructionFormatted = `
Extract information from the following phrase: {John in 80 years old} in json format.

You must format your output as a JSON value that adheres to a given "JSON Schema" instance.

"JSON Schema" is a declarative language that allows you to annotate and validate JSON documents.

For example, the example "JSON Schema" instance {{"properties": {{"foo": {{"description": "a list of test words", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}}}
would match an object with one required property, "foo". The "type" property specifies "foo" must be an "array", and the "description" property semantically describes it as "a list of test words". The items within "foo" must be strings.
Thus, the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of this example "JSON Schema". The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.

Your output will be parsed and type-checked according to the provided schema instance, so make sure all fields in your output match the schema exactly and there are no trailing commas!

Here is the JSON Schema instance your output must adhere to. Include the enclosing markdown codeblock:
json
{"type":"object","properties":{"name":{"type":"string","description":"The name of the person"},"age":{"type":"string","description":"The age of the person"}},"required":["name","age"],"additionalProperties":false,"$schema":"http://json-schema.org/draft-07/schema#"}
`;

const chain = prompt.pipe(model).pipe(parser);

const response = await chain.invoke({
  phrase: "The name of the person is John and his age is 80",
  format_instructions: parser.getFormatInstructions(),
});

console.log(response);

function getJsonFromOutput(output) {
  const validJsonstring = output?.content.match(/```json([\s\S]*?)```/);
  if (validJsonstring && validJsonstring[1]) {
    try {
      return JSON.parse(validJsonstring[1].trim());
    } catch (error) {
      console.error("Didnt get the json format output", error);
    }
  }
  return null;
}

const response2 = await model.invoke(instructionFormatted);
const extractedJson = getJsonFromOutput(response2);
console.log(extractedJson);
