# walrus operator (:=) >>>>>> assigns values to variables as part of larger expressions

print(happy := True)

food = []
while True:
    dish = input("What food you like? ").lower()
    if dish == "quit":
        break
    food.append(dish)
print(food)

foods = []
while dishes := input("What food you like? ").lower() != "quit":
    foods.append(dishes)
print(foods)