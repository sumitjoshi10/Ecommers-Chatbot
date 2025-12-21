# 🛒 E-commerce FAQ Chatbot

This is a **Streamlit-based conversational chatbot application** designed for **E-commerce platforms**.  
It intelligently routes user queries to different backends such as **FAQs**, **SQL-based product data**, and **small talk**, providing accurate and context-aware responses in real time.

The application acts as a **single conversational interface** for customers to ask questions related to products, orders, or general platform queries.

---

## 🧩 Problem Statement

E-commerce platforms receive a large volume of repetitive and diverse user queries such as:

- Product-related FAQs (return policy, delivery time, warranty, etc.)
- Data-driven questions (price, rating, availability)
- General conversational queries (greetings, casual talk)

Handling these manually or via rigid rule-based bots is:

- **Inefficient** — requires human intervention
- **Non-scalable** — grows with user traffic
- **Inflexible** — poor handling of free-text questions

---

## ✅ Solution Implemented

This project provides a **modular, AI-driven E-commerce Chatbot** that:

- Uses **semantic routing** to classify user intent
- Automatically routes queries to the correct processing pipeline:
  - **FAQ Engine**
  - **SQL Query Engine**
  - **Small Talk Handler**
- Delivers responses via an interactive **Streamlit Chat UI**

### 🧠 Query Routing Logic

| User Query Type | Handler |
|---------------|--------|
| FAQ-related | FAQ Retrieval Chain |
| Product / Data | SQL Chain |
| Greetings / Casual Talk | Small Talk Module |

---

## 🚀 Features

- 💬 Chat-style UI using **Streamlit**
- 🧭 Intent detection using a **router module**
- 📚 FAQ-based response generation
- 🗄️ SQL-powered product data querying
- 🤖 Natural conversational small talk
- 🧩 Clean, modular architecture

---


## 📸 Project Snapshots

### Architecture Design

![Architecture Design](Snapshot/snapshot.png)  
---

### App Demo

![App Demo](Snapshot//image1.png)  
---


### 🌐 Live Demo:  


👉 [Ecommerce Chatbot App](https://ecommerce-chatbot-1.streamlit.app/) 


---

## 📂 Project Structure

```text
Ecommers-Chatbot/
│
├── app/
│   ├── main.py                # 🚀 Entry point (Streamlit App)
│   ├── router.py              # Semantic query routing
│   ├── faq.py                 # FAQ query handling logic
│   ├── sql.py                 # SQL query chain
│   ├── smalltalk.py           # Small talk responses
│   └── __init__.py
│
├── resource/
│   ├── faq_data.csv           # FAQ knowledge base
│   ├── flipkart_products.db   # SQLite / MySQL database file
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore
```

## ▶️ Entry Point

The main application entry point is:

```python
app/main.py
```

This file initializes the Streamlit app, manages chat state, and routes user queries to the appropriate handler.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sumitjoshi10/Ecommers-Chatbot.git
cd Ecommers-Chatbot
```

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run app/main.py
```

---

## 🧠 Core Logic Overview

```python
route = router(query).name

if route == 'faq':
    answer = faq_query_answer(query)
elif route == 'sql':
    answer = sql_chain(query)
elif route == 'small-talk':
    answer = talk(query)
```

Each query is classified and routed dynamically, ensuring **scalability and extensibility**.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI)
- **LLM / NLP-based Router**
- **SQL (SQLite / MySQL)** for structured data
- **Pandas** for data handling

---

## 🔮 Future Enhancements

- 🔐 User authentication
- 📦 Order tracking integration
- 🧠 LLM-powered RAG (Retrieval-Augmented Generation)
- 🌐 Multi-language support
- 📊 Analytics dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch (`feature/new-feature`)
3. Commit your changes
4. Push and open a Pull Request

---

📜 **License**: Apache License 2.0

---

👤 **Author**: Sumit Joshi  
🔗 GitHub: https://github.com/sumitjoshi10

