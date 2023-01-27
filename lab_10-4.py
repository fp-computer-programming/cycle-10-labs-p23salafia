#Jan Salafia Lab 10-4 1/23/2023
names = "John", "Jane", "Bob"
def indexed_names(names):
    indexed_list = []
    for index,name in enumerate(names):
        indexed_name = str(index) + ": " + name
        indexed_list.append(indexed_name)
    return

print(indexed_names(names))