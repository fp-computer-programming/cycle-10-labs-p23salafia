#Jan Salafia Lab 10-5 1/53/2023

def add_foods(foods):
    sixth_letter = []
    not_foods = []
    short_foods = []

    for food in foods:
        try:
            if len(food) >= 6:
                sixth_letter.append(food[5])
            else:
                short_foods.append(food)
        except TypeError:
            not_foods.append(food)

    print("Sixth Letter:", str(sixth_letter))
    print("Not Foods:", str(not_foods))
    print("Short Foods:", str(short_foods))

add_foods(["potatoes", "salsa", "cherries", "banana", "apple"])
add_foods(["naan", "celery", "buckwheat", 7, "clementine"])
add_foods(["cheeseburger", True, "chicken", "rice", "radish"])