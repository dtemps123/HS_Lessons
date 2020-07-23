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

class Lawful_Neutral:
    def evaluate_round(self, opponent_previous_choices):
        if (len(opponent_previous_choices) <= 10):
            return 0
        elif (np.sum(opponent_previous_choices[-10]) >5):
            return 1
        else:
            return 0    
    def __init__(self, pid=0):
        self.name = "lawful-neutral"
        if (pid > 0):
            self.name = self.name + "-" + str(pid)

class Chaotic_Neutral:
    def evaluate_round(self, Chaos):
        Chaos = np.random.randint(0,6, size=1)
        if (Chaos % 2) ==0:
            return 0
        else:
            return 1    
    def __init__(self, pid=0):
        self.name = "chaotic-neutral"
        if (pid > 0):
            self.name = self.name + "-" + str(pid)

class Neutral_Evil:    
	def evaluate_round(self, opponent_previous_choices):
        opp_defected = (np.sum(opponent_previous_choices) > 0)
        if opp_defected or ((len(opponent_previous_choices) == 199) and (sum(opponent_previous_choices) == 0)):
            return 1
        else:
            return 0    
    def __init__(self, pid=0):
        self.name = "neutral-evil"
        if (pid > 0): 
            self.name = self.name+"-"+str(pid)