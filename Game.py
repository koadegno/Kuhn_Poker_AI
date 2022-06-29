from Deck import Deck
from Player import CHECK,FOLD,Player



class Game:
	PLAYER_ONE = 1
	PLAYER_TWO = 2

	def __init__(self) -> None:
		self.pot = 0
		self.deck = None
		self.player1 = None
		self.player2 = None

	def __set_game(self):
		"""set the deck for the game and the player card
		"""
		self.deck = Deck()

		card_1 = self.deck.pop()
		self.player1  = Player(card_1,self.PLAYER_ONE)  if self.player1 == None else self.player1.change_card(card_1)
		card_2 = self.deck.pop()
		self.player2  = Player(card_2,self.PLAYER_TWO)  if self.player2 == None else self.player2.change_card(card_2)
		
		print( self.player1, self.player2)

	def play_game(self):

		while True:
			self.__set_game()

			#Each player antes 1
			self.pot += self.player1.mise(1)
			self.pot += self.player2.mise(1)
			
			#Player 1 check or bet 
			action_player1 = self.player1.get_check_bet()
			if action_player1 in CHECK:
				action_player2 = self.player2.get_check_bet()

				if action_player2 in CHECK: # showdown for the pot of 2
					self.show_winner()
				else: # bet
					self.pot += self.player2.mise(1)

					action_player1 = self.player1.get_fold_call()

					if action_player1 in FOLD:
						self.show_winner(self.player2) # player two takes the pot of 3 
					else:
						self.pot += self.player1.mise(1)
						self.show_winner() # showdown for the pot of 4
			else: # player 1 bet
				self.pot += self.player1.mise(1)

				action_player2 = self.player2.get_fold_call()
				if action_player2 in FOLD:
					self.show_winner(self.player1) # player two takes the pot of 3 
				else:
					self.pot += self.player2.mise(1)
					self.show_winner() # showdown for the pot of 4

	def show_winner(self,winner_player : Player = None ):
		"""show the winner of this turn

		Args:
			winner_player (Player): The winner of this round if already known. Defaults to None.
		"""
		if winner_player is None:
			if self.player1.get_card() > self.player2.get_card():
				self.set_winner(self.player1)
			else:
				self.set_winner(self.player2)
		else:
			self.set_winner(winner_player,FOLD)
		
		self.pot = 0

	def set_winner(self, winner_player : Player, action : str = None):
		"""set pot for the winner 

		Args:
			winner_player (Player): the winner of this round 
			action (str): if FOLD => change the print text. Defaults to None.
		"""		
		player_number = winner_player.get_number()
		if action == FOLD:
			print(f"The player {3 - player_number} {action} so player {player_number} wins the pot of {self.pot}")
		else:
			print(f"""
Player {self.player1.get_number()} has {self.player1.get_card()} and Player {self.player2.get_number()} has {self.player2.get_card()}
Thus, Player {player_number} wins the pot of {self.pot}		
					""")
		winner_player.add_pot(self.pot)


if __name__ == "__main__":
	game = Game()
	game.play_game()