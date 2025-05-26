---
## 🧠 FOXO Knowledge Assistant

An intelligent, LangChain-powered assistant that answers user questions across **nutrition, fitness, mental wellness, weather-aware food recommendations, personal health tracking**, and **life expectancy estimation** — using internal documents, custom tools, and external search.

Built with:

* **LangChain ReAct Agent**
* **Streamlit Chat Interface**
* **Custom tools** for weather, nutrition, life expectancy, Fitbit data analysis
* **FAISS vector search** for RAG-based internal document Q\&A
* **TAVILY web search** for answering general knowledge and current event queries when internal documents are insufficient

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sainadh-Bahadursha/Foxo_Knowledge_Assistant.git
cd foxo-knowledge-assistant
```

### 2. Install Dependencies

Ensure you're using **Python 3.10+**, then install all required packages:

```bash
pip install -r requirements.txt
```

### 3. Build the Vector Index (for internal document Q\&A)

Place your documents (PDF or TXT) inside the `data/` folder, then run:

```bash
python -m vectorstore.build_vectorstore
```

### 4. Launch the App

```bash
streamlit run app.py
```

At startup, you’ll be prompted to securely enter:

* Your **OpenAI API Key**
* Your **Tavily API Key**

🔐 These are never stored or exposed — they remain in memory only for the current session.

---

## 🛠️ Tools Used & Rationale

| Tool / Component             | Purpose                                                                  |
| ---------------------------- | ------------------------------------------------------------------------ |
| **LangChain Agent (ReAct)**  | Tool-based reasoning to select the best action for each query            |
| **FAISS + OpenAIEmbeddings** | Fast document retrieval for internal FOXO content (RAG approach)         |
| **Streamlit**                | Interactive chat interface with form handling                            |
| **Custom Tools**             | `WeatherTool`, `LifeExpectancyTool`, `FoodNutritionTool`, `CSVAgentTool` |
| **Tavily Search API**        | Backup for external or current event queries                             |

---

## 💬 Example Questions & Agent Responses

### ➤ Q: *How much sleep do we need across different age groups?*

**A:** (via internal docs)

> "Adults need 7–9 hours, teenagers 8–10 hours, and children even more..."

---

### ➤ Q: *What should I eat in Mumbai today?*

**A:** (via weather + LLM)

> "It’s 35°C in Mumbai. Recommended meals: curd rice, cucumber salad, or fruit smoothies."

---

### ➤ Q: *Calculate my life expectancy?*

**A:** (triggers form)

> "Based on your inputs, your remaining life expectancy is **35 years**. You may live to about **80 years old**."

---

## ⚠️ Limitations & Future Enhancements

* Session state resets on refresh — no persistent memory yet.
* Uses sample Fitbit CSV — no user uploads (future upgrade planned).
* Rule-based calculator logic — no ML-based prediction yet.
* No authentication or multi-user sessions currently.
* If expanded:

  * Add **chat history export** (PDF/JSON)
  * Add **image-based nutrition estimator** using computer vision
  * Replace CSV agent with **BigQuery SQL agent** for scalable data querying

---

## 📁 Project Structure (Simplified)

```
├── app.py                              # Streamlit app (main entry)
├── agent/
│   ├── foxo_agent.py                   # ReAct agent definition
│   └── tool_router.py                  # Tool dispatch logic
├── tools/
│   ├── csv_agent_tool.py               # Fitbit data query tool
│   ├── food_nutrition_calculator.py    # Calorie estimator
│   ├── life_expectancy_calculator.py   # Life expectancy tool
│   ├── qa_tool.py                      # RAG-based document QA tool
│   ├── tavily_search_tool.py           # External search via Tavily
│   ├── weather_tool.py                 # Weather-based food suggester
├── vectorstore/
│   ├── build_vectorstore.py            # Index creator for internal documents
│   ├── indexer.py                      # FAISS index logic
├── data/                               # Place PDFs, TXTs, and CSVs here
├── requirements.txt                    # Package dependencies
```

---
