#Business Logic
def print_board(board):
	print('Board')
	for i in range(0,3):
		for j in range(0,3):
			if board[i][j]==0:
				print('| _ |',end = "")
			else:
				print(f'| {board[i][j]} |',end = "")
		print()

def game_over_player_won(board,current_player):
	print()
	print(f'Winner is {current_player}')
	print('Game Over')
	print_board(board)
	exit()

def check_winner(board,current_player):
	if  board[0][0]==board[1][1]==board[2][2]:
		if board[0][0]!=0:
			game_over_player_won(board,current_player)
	
	if  board[0][2]==board[1][1]==board[2][0]:
		if board[0][2]!=0:
			game_over_player_won(board,current_player)

	for i in range(0,3):
		if board[i][0]==board[i][1]==board[i][2]:
			if board[i][0]!=0:
				game_over_player_won(board,current_player)

		elif board[0][i]==board[1][i]==board[2][i]:
			if board[0][i]!=0:
				game_over_player_won(board,current_player)
		
	

def check_draw(board):
	res = any(0 in board_sublist for board_sublist in board)
	if res==False:
		print()
		print('Draw Game')
		print('Game Over')
		print_board(board)
		exit()


