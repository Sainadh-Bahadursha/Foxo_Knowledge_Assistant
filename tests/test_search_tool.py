from tools.tavily_search_tool import SearchTool
import os

def run_search_test(query: str):
    print("=" * 100)
    print(f"Query: {query}")
    tool = SearchTool()
    result = tool.search(query)
    print(f"\nResult:\n{result}")
    print("=" * 100 + "\n")

if __name__ == "__main__":
    # Run test queries
    run_search_test("Who won the last Cricket World Cup?")
    run_search_test("What are the symptoms of vitamin D deficiency?")
    run_search_test("Latest advancements in artificial intelligence 2025")
