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
			action_player2 = self.player2.get_fold_call()
			if action_player2 == FOLD:
				self.show_winner(self.player1) # player two takes the pot of 3 
			else:
				self.show_winner() # showdown for the pot of 4

if __name__ == "__main__":
	game = Game()
	game.play_game()