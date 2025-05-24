import requests
from langchain_openai import ChatOpenAI

class WeatherTool:
    def __init__(self):
        self.geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        self.weather_url = "https://api.open-meteo.com/v1/forecast"
        self.llm = ChatOpenAI(model_name="gpt-4o", temperature=0.5)

    def get_lat_lon(self, city: str):
        response = requests.get(self.geo_url, params={"name": city, "count": 1})
        data = response.json()
        if "results" in data and data["results"]:
            return data["results"][0]["latitude"], data["results"][0]["longitude"]
        return None, None

    def get_weather(self, city: str):
        lat, lon = self.get_lat_lon(city)
        if lat is None or lon is None:
            return f"Could not find weather info for '{city}'."

        response = requests.get(self.weather_url, params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        })
        weather = response.json().get("current_weather", {})
        temperature = weather.get("temperature")

        if temperature is None:
            return " Weather data unavailable."

        suggestion = self.get_food_from_llm(temperature)
        return (
            f" It is currently {temperature}°C in {city}.\n\n"
            f" Based on the weather, here's a food suggestion: {suggestion}"
        )

    def get_food_from_llm(self, temperature: float) -> str:
        prompt = (
            f"The current temperature is {temperature}°C. "
            f"Suggest a few food or drink options that are appropriate for this weather. "
            f"Keep it concise and use natural language."
        )

        try:
            response = self.llm.invoke(prompt)
            return response.content.strip()
        except Exception as e:
            return f"Failed to get food suggestion from LLM: {e}"
