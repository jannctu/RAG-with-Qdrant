import openai
import os
from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

url = "http://localhost:6333"

client = QdrantClient(
    url=url, prefer_grpc=False
)

print("##############")

collection_name = "vector_db"
embeddings_model = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_KEY"))
db = Qdrant(client=client, embeddings=embeddings_model, collection_name="vector_db")

llm = OpenAI(openai_api_key=os.getenv("OPENAI_KEY"))

retrieval_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever()
)

def ask_question(question):
    result = retrieval_qa({"query": question})
    return result['result']

if __name__ == "__main__":
    question = "Sejak kapan Mbah Santoso mulai menekui profesi sebagai dalang?"
    answer = ask_question(question)
    print("Question:", question)
    print("Answer:", answer)
