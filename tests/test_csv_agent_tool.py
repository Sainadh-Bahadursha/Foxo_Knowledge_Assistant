from tools.csv_agent_tool import CSVAgentTool

def run_csv_query_test(query: str):
    print("=" * 100)
    print(f"Query: {query}")
    
    file_path = "data/fake_fitbit.csv"  # Make sure this file exists
    tool = CSVAgentTool(file_path)
    
    result = tool.ask(query)
    print(f"\nResult:\n{result}")
    print("=" * 100 + "\n")

if __name__ == "__main__":
    run_csv_query_test("What is my average number of steps?")
    run_csv_query_test("Which day did I sleep the most?")
    run_csv_query_test("Total calories burned over the days?")
    run_csv_query_test("Compare sleep and active minutes.")
