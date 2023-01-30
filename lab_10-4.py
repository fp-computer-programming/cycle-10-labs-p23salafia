#Jan Salafia Lab 10-4 1/23/2023

def indexed_names(names_list):
    return [str(index) + ": " + name for index, name in enumerate(names_list)]


print(indexed_names(["John", "Jane", "Bob"]))                       # Test case 1
print(indexed_names(["Alice", "Bob", "Charlie", "David"]))          # Test case 2
