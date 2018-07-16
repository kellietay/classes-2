
class Player(Object):

	def __init__(self,game_piece,name):
		self.game_piece = game_piece	
		self.name = name
		
class Move(Object):

	def __init__(self,author,position):
		self.author = author
		self.position = position

class Board
