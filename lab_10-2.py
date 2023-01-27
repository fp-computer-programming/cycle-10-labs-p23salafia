#Jan Salafia Lab 10-2 1/20/2023
list = [1,2,3,4,5,6,7,8,9]
multof3 = 0

while True:                 #If there is a list
    if list[multof3] % 3 == 0:  #Find multiples of 3
        print(list[multof3])    #Print multiples of 3
    if multof3 == len(list)-1:  #If the list ends
        break                   #Break the loop
    multof3 += 1               


