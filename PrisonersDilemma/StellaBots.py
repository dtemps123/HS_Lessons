import numpy as np

class ChaoticNice:
	def evaluate_round(self, opponent_previous_choices):
		# defect on the first round
		if (len(opponent_previous_choices)==0):
			return 1

		# "lesser retaliatory strike"
		elif (np.sum(opponent_previous_choices[-10:])==0):
			return 0
		else:
			return 1

	def __init__(self, pid=0):
		self.name = "chaotic nice"
		if (pid > 0): 
			self.name = self.name+"-"+str(pid)

class LawfulGood:

	def evaluate_round(self, opponent_previous_choices):
		# don't defect on the first round
		if (len(opponent_previous_choices)==0):
			return 0

		# "lesser retaliatory strike"
		elif (np.sum(opponent_previous_choices[-10:])<5):
			return 0
		else:
			return 1

	def __init__(self, pid=0):
		self.name = "lawful-good"
		if (pid > 0): 
			self.name = self.name+"-"+str(pid)