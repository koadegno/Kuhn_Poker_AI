from Deck import Deck
from Player import CHECK,BET,FOLD,CALL, Player



class Game:
	
	def __init__(self) -> None:
		self.pot = 0
		self.deck = Deck()
		self.player1 = Player(self.deck.pop(),1)
		self.player2 = Player(self.deck.pop(),2)

	def play_game(self):
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
		if winner_player is None:
			if self.player1.get_card() > self.player2.get_card():
				self.set_winner(self.player1)
			else:
				self.set_winner(self.player2)
		else:
			self.set_winner(winner_player,"FOLD")
		
		self.pot = 0

	def set_winner(self, winner_player : Player, action : str = None):
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