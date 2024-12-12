import * as dotenv from "dotenv";

import { ChatGroq } from "@langchain/groq";
import { ChatPromptTemplate } from "@langchain/core/prompts";
import { Document } from "@langchain/core/documents";
import { createStuffDocumentsChain } from "langchain/chains/combine_documents";
import { CheerioWebBaseLoader } from "@langchain/community/document_loaders/web/cheerio";
import { RecursiveCharacterTextSplitter } from "langchain/text_splitter";
import { createRetrievalChain } from "langchain/chains/retrieval";
import { JinaEmbeddings } from "@langchain/community/embeddings/jina";
import { MemoryVectorStore } from "langchain/vectorstores/memory";
import { AIMessage, HumanMessage } from "@langchain/core/messages";

import { MessagesPlaceholder } from "@langchain/core/prompts";

dotenv.config();

const llm = new ChatGroq({
  model: process.env.MODEL,
  apiKey: process.env.GROQ_API_KEY,
});

const loader = new CheerioWebBaseLoader(
  "https://python.langchain.com/docs/concepts/lcel/"
);

const docs = await loader.load();
// console.log(docs);

const embeddings = new JinaEmbeddings({
  apiKey: process.env.JINA_API_KEY,
});

const splitter = new RecursiveCharacterTextSplitter({
  chunkSize: 100,
  chunkOverlap: 10,
});

const splitDocs = await splitter.splitDocuments(docs);

// we are using memory vector store
const vectorstore = await MemoryVectorStore.fromDocuments(
  splitDocs,
  embeddings
);

// retrieving data from vector store
const retriever = vectorstore.asRetriever({
  k: 3,
});

const rephrasePrompt = ChatPromptTemplate.fromMessages(
  new MessagesPlaceholder("chat_history"),
  ["user", "{input}"][
    ("user",
    "given the conversation generate a search query to look up in order to get information relevant to conversation")
  ]
);

// const historyAwareRetriever = await createHistoryAwareRetriever({
//   llm,
//   retriever,
//   rephrasePrompt: rephrasePrompt,
// });

const prompt = ChatPromptTemplate.fromMessages(
  ["system", "answer the following user question given the context: {context}"],
  new MessagesPlaceholder("chat_history"),
  ["user", "{input}"]
);

const documentChain = await createStuffDocumentsChain({
  llm: llm,
  prompt: prompt,
});

const retrievalChain = await createRetrievalChain({
  combineDocsChain: documentChain,
  retriever: retriever,
});

// chat history data
const chatHistory = [
  new HumanMessage("Hello"),
  new AIMessage("Hi, how can I help you?"),
  new HumanMessage("My name is Leon"),
  new AIMessage("Nice to meet you Leon"),
  new HumanMessage("What is LCEL?"),
  new AIMessage(
    "LCEL stands for Langchain Expression Language from langchain community."
  ),
];

// documentChain
const response = await retrievalChain.invoke({
  input: "what is my name?",
  chat_history: chatHistory,
});

console.log(response.answer);
