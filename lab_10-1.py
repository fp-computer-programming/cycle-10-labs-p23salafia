#Jan Salafia Lab 10-1 1/20/2023
input_number = input("Please input a number")           #Input a number
input_number = int(input_number)

sum = 0             #Define the starting sum

if input_number == -1:              #If the number os -1, terminate the program
    print(sum)

sum += input_number             #Add the input to the sum

while input_number != -1:              #When input is not -1
    x = input("Please input a number that will be added to all previous numbers: ")
    x = int(x)                          #Change the string to integer
    if x ==-1:                          #If the number is -1 terminate the loop
        print(sum)
        break
    sum += x                            #Add the sum to  the list

