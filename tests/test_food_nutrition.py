from tools.food_nutrition_calculator import FoodNutritionTool

def run_test_case(food_items):
    tool = FoodNutritionTool()
    result = tool.estimate_list(food_items)
    print("=" * 100)
    print(" Test Case:")
    for item in food_items:
        print(f"- {item['food'].title()} : {item['grams']}g")
    print("\n Result:\n")
    print(result)
    print("=" * 100 + "\n\n")

if __name__ == "__main__":
    # Test Case 1 - All known items
    run_test_case([
        {"food": "rice", "grams": 200},
        {"food": "egg", "grams": 100},
        {"food": "banana", "grams": 120}
    ])

    # Test Case 2 - Includes an unknown item
    run_test_case([
        {"food": "curd", "grams": 150},
        {"food": "burger", "grams": 200}  # not in database
    ])

    # Test Case 3 - Single item
    run_test_case([
        {"food": "paneer", "grams": 50}
    ])
