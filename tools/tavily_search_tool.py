import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class SearchTool:
    def __init__(self):
        self.api_key = st.secrets["TAVILY_API_KEY"]
        self.url = "https://api.tavily.com/search"

    def search(self, query: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"query": query, "search_depth": "advanced", "include_answer": True}

        try:
            response = requests.post(self.url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            if result.get("answer"):
                return result["answer"]
            return " Tavily couldn't find an answer."
        except Exception as e:
            return f" Tavily search failed: {str(e)}"
