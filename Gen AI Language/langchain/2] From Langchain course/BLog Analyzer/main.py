from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings.openai import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['PINECONE_API_KEY'] = os.environ['PINECONE_API_KEY']
index_name="bloganalyzer"

def load_embedding_model():
    model_name = "sentence-transformers/paraphrase-MiniLM-L6-v2"
    embeddings = SentenceTransformer(model_name)
    return embeddings


# TODO: initialize pinecone here

# pc = Pinecone(api_key="fb7d610e-c199-4f7b-a476-3f29793efd4b")
# index = pc.Index("quickstart")

if __name__ == '__main__':
    print("Blog analyzer is running...")
    
    text_file_path = "data/blog1.txt"
    
    loader = TextLoader(text_file_path, encoding="utf8")
    document = loader.load()
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    texts = text_splitter.split_documents(document)
    
    # TODO: change the embeddings to our own for free use
    # embeddings = OpenAIEmbeddings(
    #     openai_api_key="sk-1234567890abcdef1234567890abcdef",
    # )
    
    print("Loading the embedding model")
    embedding = load_embedding_model()