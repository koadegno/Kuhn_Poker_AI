

class Card:
	""" Class representing Kuhn poker card
		Thus only King ,Queen and Jack 

		Attributes:
			card_values : the values of the card
	"""

	values = ["Jack","Queen","King","####"]

	def __init__(self,card_value) -> None:
		
		if card_value < 0 or card_value > 4:
			raise TypeError("Card value must be between 0 and 3")

		self.value = card_value
	

	def __lt__(self, card_2):
		if self.value < card_2.value:
			return True
		return False

	def __gt__(self, card_2):
		return self.value > card_2.value
		

	def __eq__(self, card2: object) -> bool:
		return self.value == card2.value

	def __repr__(self): 
		return self.values[self.value] 