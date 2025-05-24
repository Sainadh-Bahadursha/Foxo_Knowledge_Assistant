class LifeExpectancyTool:
    def estimate(self, age: int, smoker: bool, exercise: bool, diet: bool, sleep: bool) -> str:
        expectancy = 80
        if smoker: expectancy -= 7
        if not exercise: expectancy -= 3
        if not diet: expectancy -= 3
        if not sleep: expectancy -= 2

        final = max(expectancy - age, 0)
        return (
                f" Based on your inputs, your estimated remaining life expectancy is **{final} years**.\n\n"
                f" You are expected to live approximately until the age of **{final + age} years**."
        )
