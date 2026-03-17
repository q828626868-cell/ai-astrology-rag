# \# AI RAG Knowledge Base

# 

# 一個基於本地大語言模型的知識庫問答系統。

# 使用者可以上傳文件，系統會從文件中找出相關內容，

# 再由本地 AI 模型生成回答，不需要連接 OpenAI 或任何外部 API。

# 

# \## 技術架構

# 

# \- \*\*Ollama\*\* － 在本地運行大語言模型（llama3）

# \- \*\*LangChain\*\* － 控制 RAG 流程與模型呼叫

# \- \*\*ChromaDB\*\* － 儲存文件向量，支援語意搜尋

# \- \*\*FastAPI\*\* － 提供 REST API 服務

# 

# \## 系統流程

# 

# 文件 → 切分 → Embedding → 向量資料庫 → 語意搜尋 → LLM 生成回答

# 

# \## 如何啟動

# 

# pip install -r requirements.txt

# python -m uvicorn main:app --reload

# 

# 啟動後開啟：http://127.0.0.1:8000

