from random import shuffle
from Card import Card

	
class Deck:
	"""Representing a deck of Kuhn Poker card
		
	"""

	MAX_CARD = 3

	def __init__(self) -> None:
		self.cards = []

		for i in range(MAX_CARD):
			self.cards.append(Card(i))
		
		shuffle(self.cards)

	
	def pop(self):
		if len(self.cards) == 0:
			return
		return self.cards.pop()