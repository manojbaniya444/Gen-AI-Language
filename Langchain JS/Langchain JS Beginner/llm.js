import { ChatGroq } from "@langchain/groq";
import * as dotenv from "dotenv";

dotenv.config();

// model define
const model = new ChatGroq({
  apiKey: process.env.GROQ_API_KEY,
  model: "llama3-8b-8192",
});

console.log("___________________SIMEPLE INVOKE____________________");
const response = await model.invoke("Hello");
console.log(response.content);

console.log("___________________BATCH INVOKE____________________");
const response2 = await model.batch(["Hello", "Who are you?"]);
console.log(response2[0].content, response2[1].content);

console.log("____________________STREAM INVOKE______________________");
const response3 = await model.stream("Write a story about a dog.");

for await (const chunk of response3){
    console.log(chunk?.content)
}