import pickle
from Card import Card
from random import randint, choices
from KuhnPokerTrainner import Node

CHECK = "check"
BET = "bet"
FOLD = "fold"
CALL = "call"

class Player:
	"""Player for the Kuhn Poker game
	"""

	ACTION = [CHECK,BET,FOLD,CALL]
	CHECK_ACTION = 0
	BET_ACTION = 1
	FOLD_ACTION = 2
	CALL_ACTION = 3
	
	
	def __init__(self,card,number) -> None:
		self.card : Card = card
		self.cash : int = 1000000
		self.wins : int = 0
		self.number : int = number

	def get_card(self) -> Card:
		return self.card

	def _get_card(self):
		return self.get_card()

	def mise(self,cash_bet):
		"""allow the player to bet cash 

		Args:
			cash_bet (int): cash bet

		Returns:
			int: the cash bet
		"""
		if self.cash >= cash_bet:
			self.cash -= cash_bet
			return cash_bet
		return None

	def get_check_bet(self,precedent_move=None):
		return self._get_action(self.CHECK_ACTION,self.BET_ACTION)
			
	def get_fold_call(self,precedent_move=None):
		return self._get_action(self.FOLD_ACTION,self.CALL_ACTION)
	
	def _get_action(self,action1,action2):
		"""get the input of the player check, bet, fold or call

		Args:
			action1 (int): number associted to the action check = 0, bet = 1 , ...
			action2 (int): number associted to the action check = 0, bet = 1 , ...

		Returns:
			string: player input
		"""
		player_action = ""
		while player_action not in (self.ACTION[action1][0],self.ACTION[action2][0]):
			player_action = input(f"Player {self.number} - Do you want to {self.ACTION[action1]} or {self.ACTION[action2]} 1 : ")
		return player_action
	
	def get_number(self):
		return self.number

	def change_card(self, card):
		self.card = card
		return self
	
	def add_pot(self,pot):
		self.cash += pot
		self.wins += 1
		
	def __repr__(self) -> str:
		string  = \
		f"""
		-------------------
		| P : {self.number}     Card : {self._get_card()}     Cash : {self.cash}     Wins : {self.wins}  
		-------------------
		"""
		return string

	def precedent_move(self):
		return

class AIPlayer(Player):
	"""Representing a player inheriting from Player 

	"""
	
	AI_FILE_NAME = "AI_strategies_*_#.pkl"

	def __init__(self, card, number,level="hard") -> None:
		super().__init__(card, number)
		ia_number = randint(1,3)
		filename = self.AI_FILE_NAME.replace('*',level.lower()).replace('#',str(ia_number))
		# print(filename)
		file = open(filename, 'rb')
		self.dict_strategies : dict = pickle.load(file,encoding="bytes")
		file.close()
		self.strategies = self.set_up_strategies()
		self.history = ""
	
	def change_card(self, card) -> Player:
		super().change_card(card)
		self.history = ""
		self.strategies = self.set_up_strategies()
		return self

	def _get_card(self) -> Card:
		return Card(3)
	
	def set_up_strategies(self):
		"""get the strategies from the dictionnary containing the strategies according to your current card

		Returns:
			dict: dictionnary containing the strategie according to the card and player 
		"""

		temporary_dict = {}
		#just get a list of items sorted
		sorted_items = sorted(self.dict_strategies.items(), key=lambda x: x[0]) 
		turn = 1
		# get only strategie for player 1
		for history, strat_proba in filter(lambda x: len(x[0]) % 2 == self.number-1, sorted_items): 
			# print()
			card_number = int(history.split()[0].strip())
			# print(history, strat_proba, card_number,sep=" *** ")
			# print()
			if self.card == Card(card_number): # get the good card strategie
				# print(strat_proba)
				temporary_dict[turn] = strat_proba
				turn+=1
		return temporary_dict

	def get_check_bet(self,precedent_move=None):
		self._add_history(precedent_move)
		return super().get_check_bet(precedent_move)
		
	def get_fold_call(self,precedent_move=None):
		self._add_history(precedent_move)
		return super().get_fold_call(precedent_move)

	def _get_action(self, action1, action2):

		turn_j1 = 1 if action1 == self.CHECK_ACTION else 2
		action_intervales = self.ACTION[0:2] if action1 == self.CHECK_ACTION else self.ACTION[2:]
		
		if len(self.history) % 2  == 0 : #player 1
			node : Node = self.strategies[turn_j1]
		else: #player 2
			# print("player 2 - turn {}".format(turn_j1%2+1))
			# strategies always inverse of turn_j1 if 1 then 2, if 2 then 1
			node : Node = self.strategies[turn_j1%2+1] 

		probalities = node.get_average_strategy()
		# print(self.history,node, self.card, probalities,sep=" * * ")
		ia_choice = choices(action_intervales,weights=probalities,k=1)[0]
		
		print(f"Player {self.number} - chooses to {ia_choice}")
		self._add_history(ia_choice[0])
		return ia_choice[0]
		

	def _add_history(self,move):
		self.history += move if move != None else self.history

	
if __name__ == "__main__":
	
	player = AIPlayer(Card(0),2,"Hard")
	
	print("resulte : ",player.get_fold_call("b"))
