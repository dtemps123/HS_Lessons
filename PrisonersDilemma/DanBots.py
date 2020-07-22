import numpy as np

class FlipACoin:	
	def evaluate_round(self, Coin):
		Coin = np.random.randint(0,100, size=1)
		if (Coin >= 50):
			return 0
		else:
			return 1	

	def __init__(self, pid=0):
		self.name = "flip-a-coin"
		if (pid > 0):
			self.name = self.name + "-" + str(pid)

class SICKO_MODE:	
	def evaluate_round(self, opponent_previous_choices):
		# If this is the first round, don't defect
		if (len(opponent_previous_choices) == 0):
			return 0
		else:
			if (sum(opponent_previous_choices) > 0):
				return 1
			else:
				return 0	

	def __init__(self, pid=0):
		self.name = "sicko-mode"
		if (pid > 0):
			self.name = self.name + "-" + str(pid)