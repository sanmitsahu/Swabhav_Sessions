def update(val):
	print(id(val))
	val = 0
	print(id(val))

x = 10
print(id(x))
update(x)
print(x)