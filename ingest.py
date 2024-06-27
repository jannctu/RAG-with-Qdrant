import openai
import os
from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

loader = PyPDFLoader("data.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splitted_docs = text_splitter.split_documents(documents)

texts = [doc.page_content for doc in splitted_docs]

# Generate embeddings for the texts
embeddings_model = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_KEY"))
embeddings = embeddings_model.embed_documents(texts)

url = "http://localhost:6333"
qdrant = Qdrant.from_texts(
    texts=texts,
    embedding=embeddings_model,
    url=url,
    prefer_grpc=False,
    collection_name="vector_db"
)

print("Vector DB Successfully Created!")
