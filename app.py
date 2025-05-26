
import streamlit as st
from agent.foxo_agent import FOXOAgent
from vectorstore.indexer import FAISSIndexer
import os

from PIL import Image

st.set_page_config(page_title="FOXO Knowledge Assistant", layout="wide")

# Load and show logo
logo_path = "data/foxoclub_logo.png"  # Update path as needed
logo = Image.open(logo_path)

col1, col2 = st.columns([1, 8])
with col1:
    st.image(logo, width = 100)
with col2:
    st.title("FOXO Knowledge Assistant")

st.markdown("""
# Welcome to the **FOXO Knowledge Assistant**

Your intelligent, multi-tool assistant for answering questions across **nutrition, mental wellness, physical activity, weather-based recommendations, and personal health tracking** — powered by advanced AI and LangChain’s ReAct Agent framework.

This assistant combines:
-  **Internal document search** from curated research on fitness, sleep, stress, and health
-  **Weather-based food suggestions** using real-time city weather data
-  **Food nutrition calculator** based on portion sizes
-  **Life expectancy estimation** using your age and lifestyle
-  **Fitness data analysis** from your uploaded Fitbit/activity CSV
-  **Web search fallback** via Tavily for current events or general questions

---

##  Try Asking:

---

###  **Health & Wellness** *(via RAG QA tool on internal FOXO documents)*
- *Summarize the "Why FOXO" and "Why Longevity" documents.*
- *How much sleep is recommended across different age groups?*
- *What are the five pillars of the FOXO company?*
- *How does stress impact mental health?*

---

### **Weather-Aware Nutrition** *(via weather_food tool)*
- *What should I eat in Delhi if it’s hot today?*
- *Suggest meals for rainy weather in Bengaluru.*

---

###  **Personal Calculators** *(via life expectancy and food nutrition calculator tools)*
- *Calculate my life expectancy?*
- *Calculate my food nutrition?*

---

###  **Fitbit/Activity Data Analysis** *(via csv agent tool)*
- *What was my average step count last week?*
- *Which day did I burn the most calories?*

---

###  **External Knowledge (via Web Search tool)**
- *Who won the last Women’s T20 World Cup?*
- *What are the symptoms of vitamin D deficiency?*


---

 Just type your question below and FOXO will automatically decide which tools to use to give you the most informed, context-aware response.

⚠️ **To get started, please enter your API keys below.** Your keys will only be used for this session and never shared.
            
"""

)
# Ask for API keys
# Step 1: Check if keys already stored in session
if "api_keys_set" not in st.session_state:
    st.session_state.api_keys_set = False

# Step 2: Show input form if not set
if not st.session_state.api_keys_set:
    with st.form("api_key_form"):
        openai_key = st.text_input("Enter your OpenAI API Key", type="password", help="Required for answering questions using AI")
        tavily_key = st.text_input("Enter your Tavily API Key", type="password", help="Used for web searches")
        submitted = st.form_submit_button("🔓 Apply API Keys")

    if submitted:
        if not openai_key or not tavily_key:
            st.error("Both API keys are required.")
        else:
            os.environ["OPENAI_API_KEY"] = openai_key
            os.environ["TAVILY_API_KEY"] = tavily_key
            st.session_state.api_keys_set = True
            st.rerun()
    st.stop()
else:
    # Already set — apply to environment for tools to pick up
    os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "")
    os.environ["TAVILY_API_KEY"] = os.environ.get("TAVILY_API_KEY", "")


# Initialize agent and states
if "foxo_agent" not in st.session_state:
    retriever = FAISSIndexer(persist_dir="vectorstore").load_index("company_knowledge_index")
    st.session_state.foxo_agent = FOXOAgent(retriever)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "awaiting_life_inputs" not in st.session_state:
    st.session_state.awaiting_life_inputs = False

if "awaiting_nutrition_inputs" not in st.session_state:
    st.session_state.awaiting_nutrition_inputs = False

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(msg["user"])
    with st.chat_message("assistant"):
        st.markdown(msg["bot"])

# User input box
user_input = st.chat_input("Ask me anything...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.foxo_agent.ask(user_input)
            st.markdown(response)

    st.session_state.chat_history.append({"user": user_input, "bot": response})

    # Trigger calculator forms based on tool hints
    if "To calculate your life expectancy" in response:
        st.session_state.awaiting_life_inputs = True
    elif "list of food items" in response:
        st.session_state.awaiting_nutrition_inputs = True

    st.rerun()

# -- Life Expectancy Form --
if st.session_state.awaiting_life_inputs:
    st.markdown("### 🧬 Life Expectancy Calculator")
    with st.form("life_form"):
        age = st.number_input("Your current age", min_value=0, max_value=120, value=30)
        smoker = st.checkbox("Do you smoke?")
        exercise = st.checkbox("Do you exercise regularly?")
        diet = st.checkbox("Do you follow a healthy diet?")
        sleep = st.checkbox("Do you get at least 7 hours of sleep per night?")
        submitted = st.form_submit_button("Calculate")

    if submitted:
        from tools.life_expectancy_calculator import LifeExpectancyTool
        result = LifeExpectancyTool().estimate(age, smoker, exercise, diet, sleep)

        st.session_state.chat_history.append({"user": "[Life Expectancy Form]", "bot": result})
        st.session_state.awaiting_life_inputs = False
        st.rerun()

# -- Nutrition Calculator Form --
if st.session_state.awaiting_nutrition_inputs:
    st.markdown("### 🍱 Nutrition Calculator")

    food_options = [
        "rice", "chapati", "egg", "chicken", "apple", "banana", "milk",
        "curd", "paneer", "fish", "dal", "potato"
    ]
    food_items = []
    count = st.number_input("Number of food items", min_value=1, max_value=10, value=3)

    with st.form("nutrition_form"):
        for i in range(count):
            col1, col2 = st.columns(2)
            with col1:
                food = st.selectbox(f"Select food {i+1}", options=food_options, key=f"food_{i}")
            with col2:
                grams = st.number_input(f"Grams {i+1}", min_value=1, max_value=1000, value=100, key=f"grams_{i}")
            food_items.append({"food": food, "grams": grams})

        submitted = st.form_submit_button("Estimate Calories")

    if submitted:
        from tools.food_nutrition_calculator import FoodNutritionTool
        result = FoodNutritionTool().estimate_list(food_items)

        st.session_state.chat_history.append({"user": "[Nutrition Form]", "bot": result})
        st.session_state.awaiting_nutrition_inputs = False
        st.rerun()
