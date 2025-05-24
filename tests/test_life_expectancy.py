from tools.life_expectancy_calculator import LifeExpectancyTool

def test_life_expectancy(age, smoker, exercise, diet, sleep):
    tool = LifeExpectancyTool()
    result = tool.estimate(age, smoker, exercise, diet, sleep)
    print("=" * 80)
    print(f"Age: {age}, Smoker: {smoker}, Exercise: {exercise}, Diet: {diet}, Sleep: {sleep}")
    print(result)
    print("=" * 80)

if __name__ == "__main__":
    # Run multiple test scenarios
    test_life_expectancy(30, smoker=False, exercise=True, diet=True, sleep=True)
    test_life_expectancy(45, smoker=True, exercise=False, diet=False, sleep=False)
    test_life_expectancy(70, smoker=True, exercise=True, diet=False, sleep=True)
