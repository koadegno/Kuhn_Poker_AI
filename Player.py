
from Card import Card

CHECK = "check"
BET = "bet"
FOLD = "fold"
CALL = "call"

class Player:

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

	def get_check_bet(self):
		return self._get_action(self.CHECK_ACTION,self.BET_ACTION)
			
	def get_fold_call(self):
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
		| P : {self.number}     Cash : {self.cash}     Wins : {self.wins}
		-------------------
		"""
		return string

	