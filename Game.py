from Deck import Deck
from Player import CHECK,FOLD, AIPlayer,Player
from KuhnPokerTrainner import Node



class Game:
	PLAYER_ONE = 1
	PLAYER_TWO = 2

	def __init__(self) -> None:
		self.pot = 0
		self.deck = None
		self.player1 = None
		self.player2 = None

	def __set_game(self, game_settings):
		"""set the deck for the game and the players cards
		"""
		self.deck = Deck()
		card_1 = self.deck.pop()
		card_2 = self.deck.pop()
		PLAYER_NUMBERS = 2
		if game_settings[0] == PLAYER_NUMBERS:
			self.player1  = Player(card_1,self.PLAYER_ONE)  if self.player1 == None else self.player1.change_card(card_1)
			self.player2  = Player(card_2,self.PLAYER_TWO)  if self.player2 == None else self.player2.change_card(card_2)
		else:
			if game_settings[1] == self.PLAYER_ONE:
				self.player1  = Player(card_1,self.PLAYER_ONE)  if self.player1 == None else self.player1.change_card(card_1)
				self.player2  = AIPlayer(card_2,self.PLAYER_TWO)  if self.player2 == None else self.player2.change_card(card_2)

			else:
				self.player1  = AIPlayer(card_1,self.PLAYER_ONE)  if self.player1 == None else self.player1.change_card(card_1)
				self.player2  = Player(card_2,self.PLAYER_TWO)  if self.player2 == None else self.player2.change_card(card_2)

		print( self.player1, self.player2)

	def home(self):
		"""Ask the settings for the games

		Returns:
			list: the list containing the settings for the games
		"""
		user_choices = []
		user_choice = self.number_player()
		user_choices.append(int(user_choice))

		if user_choice == "1":
			user_choices.append(int(self.get_player_number()))
		
		return user_choices

	def get_player_number(self):
		"""ask want the player wants to play

		Returns:
			str: 1 or 2 the player answer
		"""		
		user_choice = ""
		while user_choice not in ("1","2"):
			user_choice = input(
							"""
				Do you want to play player 1 or player 2 ?\n
					1) player 1 (1)
					2) player 2 (2)\n""").strip()
		return user_choice

	def number_player(self):
		"""ask the number of player for the game

		Returns:
			str: 1 or 2 
		"""		
		user_choice = ""
		while user_choice not in ("1","2"):
			user_choice = input("""\t\t* Welcome to the Kuhn Poker game *\n
				\t1) One player  (1)
				\t2) Two players (2)\n""").strip()
		
		return user_choice

	def play_game(self):
		game_settings = self.home()
		while True:
			self.__set_game(game_settings)

			#Each player antes 1
			self.pot += self.player1.mise(1)
			self.pot += self.player2.mise(1)
			
			#Player 1 check or bet 
			action_player1 = self.player1.get_check_bet()
			if action_player1 in CHECK:
				action_player2 = self.player2.get_check_bet(action_player1)

				if action_player2 in CHECK: # showdown for the pot of 2
					self.show_winner()
				else: # player 2 bet
					self.pot += self.player2.mise(1)

					action_player1 = self.player1.get_fold_call(action_player2)

					if action_player1 in FOLD:
						self.show_winner(self.player2) # player two takes the pot of 3 
					else:
						self.pot += self.player1.mise(1)
						self.show_winner() # showdown for the pot of 4
			else: # player 1 bet
				self.pot += self.player1.mise(1)
				print("Player 2 have to fold or call ...")
				action_player2 = self.player2.get_fold_call(action_player1)
				if action_player2 in FOLD:
					self.show_winner(self.player1) # player two takes the pot of 3 
				else:
					self.pot += self.player2.mise(1)
					self.show_winner() # showdown for the pot of 4

			input("enter")
		
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
			print(f"\nThe player {3 - player_number} {action} so player {player_number} wins the pot of {self.pot}\n")
		else:
			print(f"""
Player {self.player1.get_number()} has {self.player1.get_card()} and Player {self.player2.get_number()} has {self.player2.get_card()}
Thus, Player {player_number} wins the pot of {self.pot}		
					""")
		winner_player.add_pot(self.pot)


if __name__ == "__main__":
	game = Game()
	game.play_game()