from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from agent.tool_router import get_tools

class FOXOAgent:
    def __init__(self, retriever):
        self.llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        self.agent = initialize_agent(
            tools=get_tools(retriever),
            llm=self.llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            return_intermediate_steps=True
        )

    def ask(self, query: str) -> str:
        try:
            result = self.agent.invoke({"input": query})
            return result["output"]
        except Exception as e:
            return f"Agent failed: {e}"
