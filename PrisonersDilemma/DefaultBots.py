import numpy as np

class Player:
    def __init__(self):
        self.name = "tie"

class TitForTat:
    
    def evaluate_round(self, opponent_previous_choices):
        # If this is the first round, don't defect
        if (len(opponent_previous_choices) == 0):
            return 0
        else:
            return opponent_previous_choices[-1]
    
    def __init__(self, pid=0):
        self.name = "tit-for-tat"
        if (pid > 0): 
            self.name = self.name+"-"+str(pid)
        
class Satan:
    
    def evaluate_round(self, opponent_previous_choices):
        return 1
    
    def __init__(self, pid=0):
        self.name = "satan"
        if (pid > 0): 
            self.name = self.name+"-"+str(pid)
        
class Jesus:
    
    def evaluate_round(self, opponent_previous_choices):
        return 0
    
    def __init__(self, pid=0):
        self.name = "jesus"
        if (pid > 0): 
            self.name = self.name+"-"+str(pid)
        
class Arbitrary:
    
    def evaluate_round(self, opponent_previous_choices):
        return np.round(np.random.rand())
    
    def __init__(self, pid=0):
        self.name = "arbitrary"
        if (pid > 0): 
            self.name = self.name+"-"+str(pid)
        
class MassiveRetalitoryStrike:
    
    def evaluate_round(self, opponent_previous_choices):
        opp_defected = (np.sum(opponent_previous_choices) > 0)
        if opp_defected:
            return 1
        else:
            return 0
    
    def __init__(self, pid=0):
        self.name = "massive-retaliatory-strike"
        if (pid > 0): 
            self.name = self.name+"-"+str(pid)
        
class Tester:
    
    def evaluate_round(self, opponent_previous_choices):
        if (len(opponent_previous_choices)==0):
            return 1
        else:
            if (opponent_previous_choices[-1]==1):
                return 0
            else:
                return 1
    
    def __init__(self, pid=0):
        self.name = "tester"
        if (pid > 0): 
            self.name = self.name+"-"+str(pid)