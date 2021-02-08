items1 = [10,20,30,'Swabhav']
print(id(items1))
items2 = items1
print(id(items2))
items2[3] = 'Techlabs'
print(id(items1))
print(id(items2))
