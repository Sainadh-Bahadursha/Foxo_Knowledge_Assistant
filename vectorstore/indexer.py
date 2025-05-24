import os
from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

class FAISSIndexer:
    def __init__(self, persist_dir: str = "vectorstore"):
        self.persist_dir = persist_dir
        os.makedirs(self.persist_dir, exist_ok=True)
        self.embedding = OpenAIEmbeddings()

    def _chunk_documents(self, documents: List[Dict]) -> List[str]:
        chunks = []
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", ".", " "]
        )

        for doc in documents:
            metadata = f"\n\n[Source: {doc['filename']}, Page: {doc.get('page', 'N/A')}]"
            chunks += [chunk + metadata for chunk in splitter.split_text(doc['text'])]

        return chunks

    def create_faiss_index(self, documents: List[Dict], index_name: str):
        print(f"Creating FAISS index: {index_name}")
        texts = self._chunk_documents(documents)
        db = FAISS.from_texts(texts, self.embedding)
        db.save_local(os.path.join(self.persist_dir, index_name))

    def load_index(self, index_name: str):
        index_path = os.path.join(self.persist_dir, index_name)
        if not os.path.exists(index_path):
            raise ValueError(f"Index not found: {index_path}")
        return FAISS.load_local(index_path, self.embedding, allow_dangerous_deserialization=True)
