import fitz  # PyMuPDF
import os
from typing import List, Dict, Any

class FileLoader:
    def __init__(self, file_paths: List[str]):
        self.file_paths = file_paths
        self.documents = []

    def load_all(self) -> List[Dict[str, Any]]:
        for path in self.file_paths:
            ext = os.path.splitext(path)[-1].lower()
            if ext == ".pdf":
                self._load_pdf(path)
            elif ext == ".txt":
                self._load_txt(path)
            else:
                print(f"Unsupported file type: {path}")
        return self.documents

    def _load_pdf(self, path: str):
        doc = fitz.open(path)
        for page_num, page in enumerate(doc, start=1):
            page_text = page.get_text()
            full_text = f"Page {page_num} of {os.path.basename(path)}\n{page_text.strip()}"

            self.documents.append({
                "filename": os.path.basename(path),
                "page": page_num,
                "type": "pdf",
                "text": full_text
            })

    def _load_txt(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        self.documents.append({
            "filename": os.path.basename(path),
            "page": None,            
            "type": "txt",
            "text": content.strip()
        })
