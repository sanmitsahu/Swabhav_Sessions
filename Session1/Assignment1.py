import random
print('A Game of Chance !')
print('Rolling Dice..')
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
point = 0

if dice2+dice1 in[7,11]:
	print(f'You rolled => {dice2+dice1}')
	print('You Won')
	exit()
elif dice2+dice1 in [2,3,12]:
	print(f'You rolled => {dice2+dice1}')
	print('Craps !')
	print('You Lose')
	exit()
else:
	print(f'You rolled => {dice2+dice1}')
	point += (dice2+dice1)
	print(f'Your point is => {point}')

current_sum = 0
while current_sum!=point:
	print()
	print('Rolling Dice..')
	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)
	current_sum = dice2+dice1

	if dice2+dice1==7:
		print('You rolled a 7')
		print('You Lose!')
		exit()
	
	print(f'Your current point is => {current_sum}.')
	if current_sum!=point:
		print(f'Roll your point => {point}')

print('You rolled your point value again.')
print('You Win!')

