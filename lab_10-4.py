#Jan Salafia Lab 10-4 1/23/2023

def indexed_names(names)
    for index,value in enumerate(names)
        broken_names = [*value]                        #BReak apart names
        names= "".join(broken_names)                   #Rejoin names