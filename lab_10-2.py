#Jan Salafia Lab 10-2 1/20/2023
input_number = input("Please input a number")
input_number = int(input_number)

sum = 0

if input_number == -1:
    print(sum)

sum += input_number

while input != -1:
    x = input("Please input a number that will be added to all previous numbers: ")
    x = int(x)
    if x ==-1:
        print(sum)
        break
    sum += x

