import random
print('Guess the Number !')

def startgame():
	x = random.randint(1, 10)
	n = 0
	guess = int(input("Your Guess : "))
	n = 1
	if guess<x:
		print("Too Low")
	elif guess>x:
		print("Too High")
	else:
		print(f"You guessed it in {n} tries. ")

	while guess!=x:
		guess = int(input("Your Guess : "))
		n += 1
		if guess<x:
			print("Too Low")
		elif guess>x:
			print("Too High")
		else:
			print(f"You guessed it in {n} tries. ")
			break

ans = 'y'
while ans=='y':
	startgame()
	ans = input('Would you like to conyinue(y/n) : ')

print('Bye!')

