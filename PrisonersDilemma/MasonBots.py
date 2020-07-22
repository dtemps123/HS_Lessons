import numpy as np

class Mason1:

	def evaluate_round(self, opponent_previous_choices):
		if len(opponent_previous_choices) == 0:
			return 0
		else:
			if (1):
				return 1
			else:
				return 0

	def __init__(self, pid=0):
		self.name = "mason1"
		if (pid > 0):
			self.name = self.name+"-"+str(pid)

class Mason2:

    def evaluate_round(self, opponent_previous_choices):
        if len(opponent_previous_choices) == 0:
            return 0
        else:
            return opponent_previous_choices[-1]

    def __init__(self, pid=0):
        self.name = "mason2"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)