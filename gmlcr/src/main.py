import net

print("Type help for a list of commands.")

game = net.algorithms.chess.game()

while True:
	move = input("Your move: ")
	if move == "exit":
		break
	elif move == "fen":
		print(game.boardToFen())
	elif move == "train":
		net.train()
	elif move == "help":
		print("""
Welcome to kevlu8's GrandMaster-Level Chess Robot!
Here are a list of commands:
	exit: exits the program
	fen: prints the current board in fen notation
	train: trains the neural network
	help: prints this help message
	otherwise, it's a move in algebraic notation (e.g. e4, Nf3, etc.)
We trust that you are entering moves in the correct format, so there is no protection against invalid moves.
		""")
	else:
		game.move(move)
		print(game)