import os
from vectorstore.file_loader import FileLoader

# Define the data folder
data_folder = "data"

# Collect all supported files from data folder
file_paths = [
    os.path.join(data_folder, fname)
    for fname in os.listdir(data_folder)
    if fname.lower().endswith((".pdf", ".txt"))
]

# Check if files exist
if not file_paths:
    print("No PDF or TXT files found in the 'data/' folder.")
    exit(1)

# Load all documents
loader = FileLoader(file_paths)
documents = loader.load_all()

# Output
print(f"Loaded {len(documents)} document(s).")
for doc in documents:
    print("-" * 80)
    print(doc["filename"], doc["type"], doc.get("page", "N/A"))
    print(doc["text"][:300])  # print a snippet
