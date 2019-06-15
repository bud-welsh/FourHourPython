meal_cost = input("How much did the meal cost? ")
tax = meal_cost * .07 # 7% tax in Indiana
tip = meal_cost * .15 # 15% tip
total_cost = meal_cost + tax + tip

print("Meal " + str(meal_cost))
print("Tax " + str(round(tax, 2)))
print("Tip " + str(round(tip, 2)))
print("Total " + str(round(total_cost, 2)))