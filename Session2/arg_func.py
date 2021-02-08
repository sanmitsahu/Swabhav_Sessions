def calculate_product(*arguments):
	product = 1
	for arg in arguments:
		product *=arg
	print(product)

calculate_product(10,20,30)
calculate_product(*range(1,6,2))
calculate_product(10,20,30,50,60)