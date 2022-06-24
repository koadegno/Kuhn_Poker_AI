
class Card:
	""" Class representing Kuhn poker card
		Thus only King ,Queen and Jack 
	"""

	values = ["Jack","Queen","King"]

	def __init__(self,value) -> None:
		self.value = value
	

	def __lt__(self, card2):
		if self.value < card2.value:
			return True
		return False

	def __gt__(self, c2):
		if self.value > c2.value:
			return True
		return False

	def __repr__(self): 
		return self.values[self.value] 