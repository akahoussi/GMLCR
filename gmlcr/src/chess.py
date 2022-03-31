class game():
	def __init__(self):
		self.board = [
			['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
			['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
			['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
		]
		self.turn = 'w'
		self.enpassant = None
		self.castling = {
			'w': {'K': True, 'Q': True},
			'b': {'k': True, 'q': True}
		}
		self.halfmove = 0
		self.fullmove = 1

	def __str__(self):
		board = self.reverseBoard()
		# now we can print the board
		return '\n'.join([' '.join(row) for row in board])

	def reverseBoard(self):
		board = []
		for i in range(8):
			board.append(self.board[7-i])
		return board

	def boardToFen(self):
		board = self.reverseBoard()
		fen = ''
		for row in board:
			empty = 0
			for piece in row:
				if piece == ' ':
					empty += 1
				else:
					if empty:
						fen += str(empty)
						empty = 0
					fen += piece
			if empty:
				fen += str(empty)
			fen += '/'
		fen = fen[:-1]
		fen += ' ' + self.turn
		fen += ' '
		if self.castling['w']['K']:
			fen += 'K'
		if self.castling['w']['Q']:
			fen += 'Q'
		if self.castling['b']['k']:
			fen += 'k'
		if self.castling['b']['q']:
			fen += 'q'
		if not (self.castling['w']['K'] or self.castling['w']['Q'] or self.castling['b']['k'] or self.castling['b']['q']):
			fen += '-'
		if self.enpassant:
			fen += ' ' + self.enpassant
		else:
			fen += ' -'
		fen += ' ' + str(self.halfmove)
		fen += ' ' + str(self.fullmove)
		return fen

	def fenToBoard(self, fen):
		fen = fen.split()
		self.board = []
		for i in range(8):
			self.board.append(fen[0][i*2:i*2+2])
		self.turn = fen[1]
		self.enpassant = fen[2]
		self.castling = {
			'w': {'K': True, 'Q': True},
			'b': {'k': True, 'q': True}
		}
		for i in range(4):
			if fen[3][i] in 'KQkq':
				self.castling[self.turn][fen[3][i]] = False
		self.halfmove = int(fen[4])
		self.fullmove = int(fen[5])

	def move(self, move):
		locs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		pieces = ['r', 'n', 'b', 'q', 'k']
		i = 0
		column = int(move[1])
		if move[0].lower() in pieces:
			# non-pawn move
			for char in locs:
				if char == move[1]:
					break
				i += 1
			pass
		else:
			# pawn move
			for char in locs:
				if char == move[0]:
					break
				i += 1
			# need to subtract 1 from the column because the board is indexed from 0
			if self.turn == 'w':
				if self.board[column - 1 - 2][i] == 'P': # 2 spaces ahead
					self.board[column - 1 - 2][i] = ' '
					self.board[column - 1][i] = 'P'
				else:
					# moved 1 square forward
					self.board[column - 1 - 1][i] = ' '
					self.board[column - 1][i] = 'P'
			else:
				if self.board[column - 1 + 2][i] == 'p':
					self.board[column - 1 + 2][i] = ' '
					self.board[column - 1][i] = 'p'
				else:
					# moved 1 square forward
					self.board[column - 1 + 1][i] = ' '
					self.board[column - 1][i] = 'p'
		self.turn = 'b' if self.turn == 'w' else 'w'

def IUSEDTHISIMPORTSODEEPSOURCEWILLSTOPYELLINGATME():
	return 0

# awh yeah, coded in python with no libraries 😎