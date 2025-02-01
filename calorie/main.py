from flask import Flask, request, render_template
from utils import get_calories, suggest_food_intake

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        total_calories = 0
        food_items = []

        food_names = request.form.getlist("food")  # List of food names
        quantities = request.form.getlist("quantity")  # Corresponding quantities

        for food, quantity in zip(food_names, quantities):
            if food.strip() and quantity.strip().isdigit():
                quantity = float(quantity)  # Convert to number
                calories_per_unit = get_calories(food)
                if calories_per_unit is not None:
                    total_food_calories = round(calories_per_unit * quantity, 2)
                    food_items.append(f"{quantity} x {food}: {round(total_food_calories)} kcal")
                    total_calories += total_food_calories

        # Calculate remaining calories & suggested intake
        remaining_calories, suggestions = suggest_food_intake(total_calories)

        return render_template(
            "result.html", 
            food_items=food_items, 
            total_calories=total_calories, 
            remaining_calories=remaining_calories, 
            suggestions=suggestions
        )

    return render_template("index.html")  # Show the input form for GET requests

if __name__ == "__main__":
    app.run(debug=True)