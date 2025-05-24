import os
from vectorstore.file_loader import FileLoader
from vectorstore.indexer import FAISSIndexer

# Step 1: Load all documents in the "data/" folder
data_folder = "data"
document_paths = [
    os.path.join(data_folder, f)
    for f in os.listdir(data_folder)
    if f.lower().endswith((".pdf", ".txt"))
]

if not document_paths:
    print("No supported documents found in 'data/' folder.")
    exit(1)

# Step 2: Load documents
loader = FileLoader(document_paths)
documents = loader.load_all()

# Step 3: Create the FAISS index
indexer = FAISSIndexer(persist_dir="vectorstore")
indexer.create_faiss_index(documents, index_name="company_knowledge_index")

print("Vector store created at: vectorstore/company_knowledge_index")
