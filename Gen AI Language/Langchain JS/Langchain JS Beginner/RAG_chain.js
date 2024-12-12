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

dotenv.config();

const llm = new ChatGroq({
  model: process.env.MODEL,
  apiKey: process.env.GROQ_API_KEY,
});

const loader = new CheerioWebBaseLoader(
  "https://aws.amazon.com/what-is/large-language-model/"
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
  k: 5,
});

// const retrievalChain = await createRetrievalChain({
//   combineDocsChain: documentChain,
//   retriever: retriever,
// });

const prompt = ChatPromptTemplate.fromTemplate(`
    Answer the user question:

    Context: {context}

    Question: {input}
    `);

// const chain = prompt.pipe(llm);

const documentChain = await createStuffDocumentsChain({
  llm: llm,
  prompt: prompt,
});

// manually creating document
// const documentA = new Document({
//   pageContent: "John Doe is a Software Engineer.",
// });

// const documentB = new Document({
//   pageContent: "John Doe is 80 years old.",
// });

const retrievalChain = await createRetrievalChain({
  combineDocsChain: documentChain,
  retriever: retriever,
});

// documentChain
const response = await retrievalChain.invoke({
  input: "what is llm?",
//   context: automatically get from retrieval chain
});

console.log(response);
