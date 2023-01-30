
def add_nums(numbers):
    while True:
        user_input = input("Enter a number: ")
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number on a keypad.")
            print("passed list: " + str(numbers) + " user input: " + str(user_input))
    result = [num + user_input for num in numbers]
    print("passed list: " + str(numbers) + " user input: " + str(user_input))
    print(result)

print(add_nums([1, 2, 3, 4]))                 #Test case 1
print(add_nums([1, 2, 3, 4.1]))               #Test case 2
print(add_nums([1, 2, 3, True]))              #Test case 3