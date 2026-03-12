from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# 載入文件
loader = TextLoader("docs/company.txt", encoding="utf-8")
documents = loader.load()

# 切分文件
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
texts = text_splitter.split_documents(documents)

# 文字轉向量
embeddings = HuggingFaceEmbeddings()

# 建立向量資料庫
db = Chroma.from_documents(texts, embeddings)

# 本地模型
llm = Ollama(model="llama3")

# RAG問答
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)

# 測試問題
question = "幾點上班？"
result = qa.run(question)

print(result)