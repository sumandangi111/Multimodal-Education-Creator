# 🎓 Multimodal Education Creator (RAG-Based Learning App)

## 📌 Project Overview

This project is a **Flask-based Multimodal Education System** that uses **Retrieval-Augmented Generation (RAG)** to generate educational content based on user queries.

It combines:

* 📚 Context retrieval (ChromaDB)
* 🤖 LLM response generation (Groq - Llama 3)
* 🖼️ Image generation (Wikipedia API)

---

## 🚀 Features

* 🔐 User Login System (Session-based authentication)
* 📖 Topic-based explanation generation
* 🧠 RAG pipeline for accurate answers
* 🗂️ Vector database using ChromaDB
* 🧾 Knowledge base from text files
* 🖼️ Image generation for better understanding

---

## 🏗️ Tech Stack

* **Backend:** Flask (Python)
* **LLM:** Groq API (Llama 3)
* **Embeddings:** HuggingFace (all-MiniLM-L6-v2)
* **Vector DB:** ChromaDB
* **Frontend:** HTML, CSS
* **Libraries:** LangChain, python-dotenv

---

## 📂 Project Structure

```
multimodal-education-creator/
│
├── app.py
├── config.py
├── ingest.py
├── add_pdf_manual.py
│
├── modules/
│   ├── llm_generator.py
│   ├── image_generator.py
│   ├── vector_store.py
│
├── templates/
├── static/
├── data/
├── uploads/
├── vector_db/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works (RAG Flow)

1. User enters a topic/query
2. Query is converted into embeddings
3. ChromaDB retrieves relevant context
4. Context + Query is sent to LLM (Groq - Llama 3)
5. LLM generates a detailed explanation
6. Related images are fetched
7. Output is displayed on UI

---

## 🔐 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_key
HUGGINGFACE_API_KEY=your_key
SECRET_KEY=your_secret
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🎯 Key Concepts Used

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* Large Language Models (LLM)
* Session Management in Flask

---

## 📌 Future Improvements

* PDF upload for dynamic knowledge base
* Advanced UI (React)
* Multi-language support
* Voice-based interaction

---

---

## ⭐ Conclusion

This project demonstrates how **RAG + LLM + Vector Databases** can be combined to build an intelligent education system that provides accurate and context-aware learning content.
