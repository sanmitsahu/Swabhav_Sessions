import random
count = [0,0,0,0,0,0]
for i in range(0,100):
	x = random.randint(1,6)
	count[x-1] +=1
for i in range(1,7):
	print(f"{i} ==> {count[i-1]}")

