import requests
from config import CALORIE_NINJAS_API_KEY, CALORIE_NINJAS_URL

DAILY_CALORIE_GOAL = 2000  # Modify this if needed

def get_calories(food_name):
    """Fetches calories per unit for a given food item."""
    headers = {"X-Api-Key": CALORIE_NINJAS_API_KEY}
    params = {"query": food_name}
    
    response = requests.get(CALORIE_NINJAS_URL, headers=headers, params=params)
    data = response.json()
    
    if "items" in data and len(data["items"]) > 0:
        return data["items"][0]["calories"]  # Returns calories per unit (100g or per serving)
    
    return None  # If no data found

def suggest_food_intake(current_calories):
    """Suggests food to meet the daily caloric intake goal."""
    remaining_calories = DAILY_CALORIE_GOAL - current_calories

    if remaining_calories <= 0:
        return 0, ["You have met or exceeded your daily caloric goal!"]

    food_options = {
        "Rice (1 cup)": 200,
        "Banana (1 medium)": 105,
        "Egg (1 large)": 70,
        "Chicken Breast (100g)": 165,
        "Milk (1 glass)": 150,
        "Apple (1 medium)": 95
    }

    suggestions = []
    for food, cal in food_options.items():
        if remaining_calories <= 0:
            break
        portions = round(remaining_calories / cal, 1)  # Calculate portions needed
        if portions > 0:
            suggestions.append(f"{portions} x {food}")

    return remaining_calories, suggestions