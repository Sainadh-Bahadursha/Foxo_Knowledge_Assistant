from tools.weather_tool import WeatherTool

def test_city_weather(city: str):
    tool = WeatherTool()
    result = tool.get_weather(city)
    print("=" * 80)
    print(f" Test City: {city}")
    print(result)
    print("=" * 80)

if __name__ == "__main__":
    test_cities = ["Delhi", "New York", "Tokyo", "Reykjavik", "Chennai"]
    for city in test_cities:
        test_city_weather(city)
