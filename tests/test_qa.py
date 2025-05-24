from vectorstore.indexer import FAISSIndexer
from tools.qa_tool import QATool

indexer = FAISSIndexer(persist_dir="vectorstore")
retriever = indexer.load_index("company_knowledge_index")

qa = QATool(retriever)
response = qa.ask("How does nutrition affect mental health?")
# response = qa.ask("How to connect fitbit data to FOXO dashboard?")
print("\n Answer:\n", response["answer"])
print("\n Sources:")
for s in response["sources"]:
    print("-" * 60)
    print(s["content"])
