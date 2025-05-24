from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from langchain_openai import ChatOpenAI
from typing import List
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

DEFAULT_PROMPT = PromptTemplate.from_template(
    """Use the context below to answer the question. 
If you don't know the answer, say "I don't know" instead of making it up.
\n\nContext:\n{context}\n\nQuestion:\n{question}\nAnswer:"""
)

class QATool:
    def __init__(self, retriever):
        self.llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0,
        )
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=retriever.as_retriever(search_type="mmr", search_kwargs={"k": 6}),
            return_source_documents=True,
            chain_type_kwargs={"prompt": DEFAULT_PROMPT}
        )

    def ask(self, query: str) -> dict:
        result = self.qa_chain({"query": query})
        sources: List[Document] = result["source_documents"]

        return {
            "answer": result["result"],
            "sources": [
                {
                    "content": doc.page_content,
                    "metadata": doc.metadata
                } for doc in sources
            ]
        }
