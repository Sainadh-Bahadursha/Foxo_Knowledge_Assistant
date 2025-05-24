class FoodNutritionTool:
    def __init__(self):
        self.calories_per_100g = {
            "rice": 130, "chapati": 104, "egg": 155, "chicken": 239, "apple": 52,
            "banana": 89, "milk": 60, "curd": 98, "paneer": 265, "fish": 206,
            "dal": 116, "potato": 77
        }

    def estimate_list(self, food_items: list[dict]) -> str:
        total_cal = 0
        output_lines = []

        for item in food_items:
            name = item.get("food", "").lower()
            grams = item.get("grams", 0)

            if name not in self.calories_per_100g:
                output_lines.append(f" Unknown food item: **{name}**")
                continue

            cal = (grams / 100) * self.calories_per_100g[name]
            total_cal += cal

            output_lines.append(
                f" *{name.title()}* ({grams}g): **{cal:.2f} kcal** "
                f"({self.calories_per_100g[name]} kcal/100g)"
            )

        output_lines.append(f"\n **Total Estimated Calories: {total_cal:.2f} kcal**")
        return "\n".join(output_lines)
