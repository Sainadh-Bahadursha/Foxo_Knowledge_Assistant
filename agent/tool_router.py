from langchain.agents import Tool
from tools.qa_tool import QATool
from tools.tavily_search_tool import SearchTool
from tools.weather_tool import WeatherTool
from tools.life_expectancy_calculator import LifeExpectancyTool
from tools.food_nutrition_calculator import FoodNutritionTool
from tools.csv_agent_tool import CSVAgentTool

def get_tools(retriever):
    qa_tool = QATool(retriever)
    search_tool = SearchTool()
    weather_tool = WeatherTool()
    csv_tool = CSVAgentTool("data/fake_fitbit.csv")

    return [
        Tool(
            name="DocumentQA",
            func=lambda q: qa_tool.ask(q)["answer"],
            description="Use this to answer questions about internal health and wellness documents."
        ),
        Tool(
            name="WebSearch",
            func=search_tool.search,
            description="Use this for general knowledge, current events, or when DocumentQA is insufficient."
        ),
        Tool(
            name="WeatherFood",
            func=weather_tool.get_weather,
            description="Get the current weather in a city and suggest food based on the temperature."
        ),
        Tool(
            name="LifeExpectancyCalculator",
            func=lambda _: (
                "To calculate your life expectancy, please provide the following information: "
                "your age, smoker status, exercise habits, diet, and sleep habits."
            ),
            description="Estimates life expectancy using age, smoking, exercise, diet, and sleep."
        ),
        Tool(
            name="NutritionCalculator",
            func=lambda _: "Please enter a list of food items and their portion sizes in grams.",
            description="Estimates calories based on food and quantity input."
        ),
        Tool(
            name="FitnessCSVAgent",
            func=csv_tool.ask,
            description="Use this to answer questions about your Fitbit/activity CSV data."
        )
    ]
