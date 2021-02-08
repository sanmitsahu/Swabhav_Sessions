import random

random_nos = [random.randint(1,5) for i in range(10)]
print(random_nos)

listoflists = [[1,2,3],[4,5,6],[7,8,9]]
results = [ ele 
			for sublist in listoflists
				for ele in sublist]
print(results)