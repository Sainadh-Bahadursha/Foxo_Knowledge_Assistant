from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI
import os

class CSVAgentTool:
    def __init__(self, file_path: str):
        self.agent = create_csv_agent(
            llm=ChatOpenAI(model_name="gpt-4o", temperature=0,openai_api_key=os.getenv("OPENAI_API_KEY")),
            path=file_path,
            verbose=False,
            allow_dangerous_code=True  
        )

    def ask(self, query: str) -> str:
        try:
            return self.agent.run(query)
        except Exception as e:
            return f" CSV Agent failed: {str(e)}"
