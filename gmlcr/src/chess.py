
class board():
	def __init__(self):
		self.board = [
			['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
			['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
			['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
			['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
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
		return '\n'.join([' '.join(row) for row in self.board])

	def boardToFen(self):
		fen = ''
		for row in self.board:
			empty = 0
			for piece in row:
				if piece == ' ':
					empty += 1
				else:
					if empty:
						fen += str(empty)
						empty = 0
					fen += piece.lower()
			if empty:
				fen += str(empty)
			fen += '/'
		fen = fen[:-1]
		fen += ' ' + self.turn
		if self.enpassant:
			fen += ' ' + self.enpassant
		fen += ' ' + '-'.join([x for x in ['KQkq', '-', '0', '1'] if x in self.castling[self.turn]])
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
		raise NotImplementedError