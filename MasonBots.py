import numpy as np

class Mason:

    def evaluate_round(self, opponent_previous_choices):
		if len(opponent_previous_choices) == 0:
			return 0
		else:
			if (1):
				return 1
			else:
				return 0

	def __init__(self, pid=0):
		self.name = "Mason"
		if (pid > 0):
			self.name = self.name+"-"+str(pid)