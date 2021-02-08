def print_board():
	print('Board')
	for i in range(0,3):
		for j in range(0,3):
			if board[i][j]==0:
				print('| _ |',end = "")
			else:
				print(f'| {board[i][j]} |',end = "")
		print()

def game_over_player_won():
	print()
	print(f'Winner is {current_player}')
	print('Game Over')
	print_board()
	exit()

def check_winner():
	if  board[0][0]==board[1][1]==board[2][2]:
		if board[0][0]!=0:
			game_over_player_won()
	
	if  board[0][2]==board[1][1]==board[2][0]:
		if board[0][2]!=0:
			game_over_player_won()

	for i in range(0,3):
		if board[i][0]==board[i][1]==board[i][2]:
			if board[i][0]!=0:
				game_over_player_won()

		elif board[0][i]==board[1][i]==board[2][i]:
			if board[0][i]!=0:
				game_over_player_won()
		
	

def check_draw():
	res = any(0 in board_sublist for board_sublist in board)
	if res==False:
		print()
		print('Draw Game')
		print('Game Over')
		print_board()
		exit()


board = [[0,0,0],[0,0,0],[0,0,0]]

current_player = 'nought'

while True:
	print()
	print_board()
	print(f'Current player is => {current_player}')
	row_position  = int(input("Enter row position(0-2) : "))
	column_position  = int(input("Enter column position(0-2) : "))

	if row_position not in[0,1,2] or column_position not in[0,1,2]:
		print('Incorrect board poistion entered. Please Enter again !')
		continue
	if board[row_position][column_position]!=0:
		print('Position already occupued! Choose Another Position')
		continue
	

	if current_player=='cross':
		board[row_position][column_position] = 'X'
	else:
		board[row_position][column_position] = 'O'
	check_draw()
	check_winner()
	
	if current_player=='nought':
		current_player = 'cross'
	else:
		current_player = 'nought'
