from fastapi import FastAPI
from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# ===== 初始化RAG =====

loader = TextLoader("docs/stars.txt", encoding="utf-8")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=60)
texts = text_splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings()

db = Chroma.from_documents(texts, embeddings)

llm = Ollama(model="qwen2.5:7b")

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)

# ===== API =====

@app.get("/")
def index():
    return FileResponse("index.html")

@app.get("/ask")
def ask(question: str):
    result = qa.invoke(question)
    return {"answer": result["result"]}