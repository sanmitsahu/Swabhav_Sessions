#Game Controller
from game import print_board,check_draw,check_winner

def tic_tac_toe():
	board = [[0,0,0],[0,0,0],[0,0,0]]
	current_player = 'nought'
	while True:
		print()
		print_board(board)
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
		check_draw(board)
		check_winner(board,current_player)
		
		if current_player=='nought':
			current_player = 'cross'
		else:
			current_player = 'nought'

if __name__=="__main__": 
	tic_tac_toe()