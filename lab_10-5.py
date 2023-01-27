#Jan Salafia Lab 10-5 1/53/2023

def add_foods(list):
    sixth_letter = []
    TEindex = 0
    try:
        for index, value in enumerate(list):
            TEindex = index
            letter_list = [*value]
            sixth_letter.append(letter_list[5])
            print("The sixth letter is " + letter_list)
    except TypeError:
        print("Invalid Input")
    except IndexError:
        print(value + " is a short food")
    return

add_foods(["potatoes", "salsa", "cherries", "banana", "apple"])
add_foods(["naan", "celery", "buckwheat", 7, "clementine"])
add_foods(["cheeseburger", True, "chicken", "rice", "radish"])