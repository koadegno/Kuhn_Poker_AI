
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
		self.card = card
		self.cash = 1000000
		self.wins = 0
		self.number = number

	def get_card(self) -> Card:
		return self.card

	def mise(self,mise):
		if self.cash >= mise:
			self.cash -= mise
			return mise
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
	
	def get_number(self) -> int:
		return self.number
	
	def add_pot(self,pot) -> None:
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

	