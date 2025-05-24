## 🧠 FOXO Knowledge Assistant

An intelligent, LangChain-powered assistant that answers user questions across **nutrition, fitness, mental wellness, weather-aware food recommendations, personal health tracking**, and **life expectancy estimation** — using internal documents, custom tools, and external search.

Built with:

* **LangChain ReAct Agent**
* **Streamlit Chat Interface**
* **Custom tools** for weather, nutrition, life expectancy, Fitbit data analysis
* **FAISS vector search** for RAG-based internal document Q&A
* **TAVILY web search** for answering general knowledge and current event queries when internal documents are insufficient

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sainadh-Bahadursha/Foxo_Knowledge_Assistant.git
cd foxo-knowledge-assistant
```

### 2. Install Dependencies

Make sure you’re using Python 3.10+, then:

```bash
pip install -r requirements.txt
```

### 3. Set Environment Secrets

Create a `.streamlit/secrets.toml` file:

```toml
OPENAI_API_KEY = "Paste-your-openai-api-key"
TAVILY_API_KEY = "Paset-your-tavily-api-key"
```

### 4. Build the Vector Index (for internal document Q\&A)

Put your documents (PDF/TXT) in the `data/` folder, then run:

```bash
python -m vectorstore.build_vectorstore
```

### 5. Launch the Chat App

```bash
streamlit run app.py
```

---

## 🛠️ Tools Used & Rationale

| Tool / Component             | Purpose                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------------|
| **LangChain Agent (ReAct)**  | Tool-based reasoning to decide which tool to use for each query                  |
| **FAISS + OpenAIEmbeddings** | Fast document search for internal foxo company and health-related content (RAG)  |
| **Streamlit**                | Clean, interactive chat interface                                                |
| **Custom Tools**             | `WeatherTool`, `LifeExpectancyTool`, `FoodNutritionTool`, `CSVAgentTool`         |
| **Tavily Search API**        | Fallback for external, current event queries                                     |

---

## 💡 Example Questions & Agent Responses

### ➤ Q: *How much sleep do we need across different age groups?*

**A:** Uses internal documents →
*"Adults need 7–9 hours, teenagers 8–10 hours, and children even more..."*

---

### ➤ Q: *What should I eat in Mumbai today?*

**A:** Uses weather API + LLM →
*"It’s 35°C in Mumbai. Recommended meals: curd rice, cucumber salad, or fruit smoothies."*

---

### ➤ Q: *Calculate my life expectancy?*

**A:** Interactive form triggers →
*"Based on your inputs, your remaining life expectancy is **35 years**. You may live to about **80 years old**."*

---

## ⚠️ Limitations & Future Improvements

* **Session memory is not persistent** — it resets on refresh.
* **Uses sample Fitbit data (not real user uploads)** — currently hardcoded to fake_fitbit.csv for demonstration purposes.
* **Form handling is rule-based**, not Machine Learning or Deep Learning driven prediction.
* No authentication or multi-user session tracking yet.
* If more time:
  * Implement chat history export in PDF or JSON format for session review or reporting
  * Integrate food image-based calorie estimation using computer vision models for real-time nutrition insights
  * Replace the CSV-based agent with a BigQuery-powered SQL agent to handle large-scale fitness and health data more efficiently

---

## 📁 Folder Structure (simplified)

```
├── app.py                              # Streamlit frontend
├── agent/
│   ├── foxo_agent.py                   # ReAct Agent with memory
│   └── tool_router.py                  # All tool definitions
├── tools/                              # Custom tools
│   ├── csv_agent_tool.py               # Tool for querying fitbit data
│   ├── food_nutrition_calculator.py    # Tool for calculating calorie count of food taken
│   ├── life_expectancy_calculator.py   # Tool for calculating your life expectancy based on some questions
│   ├── qa_tool.py                      # Tool for answering the questions on internal documents using RAG approach
│   ├── tavily_search_tool.py           # Tool for answering any external questions or current event questions
│   ├── weather_tool.py                 # Tool for LLM based food recommendation using open-meteo weather api search with respect to city provided
├── vectorstore/                        # FAISS index + loader
│   ├── build_vectorstore.py            # Company runs this file to create local vector_store of all company documents
│   ├── indexer.py                      # FAISS Indexer
├── data/                               # Store all of your company documents in this folder (PDFs, TXT, CSVs)
├── requirements.txt                    # All the required libraries with specific versions
```
