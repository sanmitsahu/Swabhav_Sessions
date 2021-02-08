import random
print('Lets Play PIG!')
print()
print('See how many turns it takes you to get to 20.') 
print('* Turn ends when you hold or roll a 1.')
print('* If you roll a 1, you lose all points for the turn.')
print('* If you hold, you save all points for the turn.')

turn = 1
score = 0
choice = 'r'
old_choice_hold = False

while score<20:
	print(f"TURN {turn}")
	if choice=='h':
		choice = input('Roll or hold? (r/h): ')
		if choice not in['r','h']:
			choice = 'h'
		old_choice_hold = True

	while choice=='r':
		if old_choice_hold==False:
			choice = input('Roll or hold? (r/h): ')

		old_choice_hold = False

		if choice=='r':
			dice = random.randint(1, 6)
			print(f"Die : {dice}")
			if dice==1:
				print('Turn over. No score.')
				score = 0
				break
			else:
				score += dice

		elif choice=='h':
			print(f'Total Score : {score}')
			continue

		else:
			print('Invalid Choice')
			choice = 'h'
			continue
	turn += 1
	print()

print(f'You finished in {turn-1} turns!')
print()
print('Game over!')
