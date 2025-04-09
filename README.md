# 🧠 Local RAG System using Mistral + Sentence Transformers + FAISS

This project is a **lightweight, fully local Retrieval-Augmented Generation (RAG)** system using:

- 🧩 [Mistral 7B](https://mistral.ai/news/announcing-mistral-7b) (run locally via `llama-cpp-python`)
- 🔍 Sentence Transformers (`all-MiniLM-L6-v2`) for semantic chunk embeddings
- 🧠 FAISS for fast similarity search
- 📄 Support for both **file-based** and **web URL** context
- 💬 Command-line chat interface with contextual answers

---
## Demo Video


https://github.com/user-attachments/assets/a880a5db-759d-42e4-8dd2-2091877b445d


---

## 🔍 Retrieval-Augmented Generation with Mistral LLM
This project demonstrates how to build a lightweight, offline-capable RAG system using:

- 🧠 A local Mistral 7B LLM (GGUF format)

- 🔎 Context retrieval using FAISS + Sentence Transformers

- 🌐 Optional web URL scraping or local text files

- 🛠 No Hugging Face APIs — 100% free and local

---

## 📦 Features

- 🔌 No API keys or cloud dependencies – everything runs **offline**
- 🌐 Ingest text from **URLs** (via web scraping) or **local `.txt` files**
- 🔎 Efficient semantic search with FAISS
- 💡 Powered by a local `GGUF` version of **Mistral 7B**

---

## 🚀 Installation

1. **Clone the repo**
```bash
git clone https://github.com/your-username/Local-RAG-System-using-Mistral-Sentence-Transformers-FAISS.git
cd local-mistral-rag
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download a Mistral GGUF Model**

You can get one from Hugging Face:

- [TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

Place it in your preferred folder and copy the path to the `.gguf` file.

---

## 📁 Project Structure

```
.
├── utils/
│   ├── embedder.py             ← Embedding + FAISS index logic
│   ├── file_loader.py          ← Load plain text files
│   ├── web_scraper.py          ← Extract text from webpages
│   └── mistral_interface.py    ← Prompt Mistral using llama-cpp
├── rag_main.py                 ← Main CLI script to run RAG system
├── requirements.txt
└── README.md
```

---

## 🧠 Usage

### 📝 Load from a local text file
```bash
python main.py --file path/to/text.txt --model_path path/to/mistral-model.gguf
```

### 🌐 Load from a web URL
```bash
python main.py --url "https://example.com/article" --model_path path/to/mistral-model.gguf
```

Then ask questions in the command line!

```txt
Ask a question (or type 'exit'): What is the main idea of the article?
```

---

## 🛠 Requirements

- Python 3.8+
- A system with 8GB+ RAM (for faster performance)
- `llama-cpp-python` with CPU or GPU support

---

## ⚙️ Advanced Tips

- You can increase the context window of Mistral up to **32768 tokens**:
```python
Llama(model_path=model_path, n_ctx=8192)
```

- To improve semantic matching, replace the embedder model with a larger SentenceTransformer if needed.

---

## ✅ Example Use Case

- Ask questions based on downloaded PDFs converted to text.
- Summarize large blog posts or research papers.
- Run it 100% offline for privacy-focused applications.

---

## 🙌 Credits

- [Mistral 7B](https://mistral.ai/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [SentenceTransformers](https://www.sbert.net/)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

---
