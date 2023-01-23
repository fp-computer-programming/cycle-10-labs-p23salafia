#Jan Salafia Lab 10-3 1/23/2023
def double_stuff(numbers):                          #Define the function
    for index,value in enumerate(numbers):          #Enumerate list
        numbers[index] = value*2                    
    return numbers

print(double_stuff([1,2,3]))                        #Test for integers
print(double_stuff([1,2.0,3]))                      #Test for integer and float values
print(double_stuff([1,2.0,"test"]))                 #Test for integer, strings, and float values
