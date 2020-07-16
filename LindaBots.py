import numpy as np
class GrumpySquidward:
	
	def evaluate_round(self, opponent_previous_choices):
			return 1
		
	def __init__(self, pid=0):
		self.name = "grumpy-squidward"
		if (pid > 0):
			self.name+"-"+str(pid)

class BandwagonerSpongebob:
	
	def evaluate_round(self, opponent_previous_choices):
		if (len(opponent_previous_choices)==0):
			return 1
		else:
			return sum(opponent_previous_choices) / 2 #chooses whatever is most popular with the opponent
		
	def __init__(self, pid=0):
		self.name = "bandwagoner-spongebob"
		if (pid > 0):
			self.name+"-"+str(pid)

