import numpy as np

#four classes for the game:
class Calvin: # aka space cadet
    def evaluate_round(self, opponent_previous_choices):
        # Your logic for deciding when to defect and when to remain goes here
        if (len(opponent_previous_choices)<2):
            return np.int(np.round(np.random.random_sample()))  ## you decide to defect
        else:
            return opponent_previous_choices[-2]  ## you decide to remain
    def __init__(self, pid=0):
        self.name = "calvin"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)

class Susan: # aka fool me twice
    def evaluate_round(self, opponent_previous_choices):
        # Your logic for deciding when to defect and when to remain goes here
        if (len(opponent_previous_choices) > 1):
            if (opponent_previous_choices[-2] == opponent_previous_choices[-1]):
                self.mood = opponent_previous_choices[-1]
        return self.mood
    def __init__(self, pid=0):
        self.name = "susan"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)
        self.mood = np.int(0)

class Christy: # aka slow to anger
    def evaluate_round(self, opponent_previous_choices):
        thisroll = np.random.random_sample()
        if (len(opponent_previous_choices) > 0):
            self.threshold = self.threshold + 0.2 * (0.5 - opponent_previous_choices[-1])
        if (self.threshold > 1):
            self.threshold = np.float64(1);
        if(self.threshold < 0):
            self.threshold = np.float64(0);
        # Your logic for deciding when to defect and when to remain goes here
        if (thisroll > self.threshold):
            return 1  ## you decide to defect
        else:
            return 0  ## you decide to remain
    def __init__(self, pid=0):
        self.name = "christy"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)
        self.threshold = np.float64(1);

class Eric: # aka pushover
    def evaluate_round(self, opponent_previous_choices):
        if (len(opponent_previous_choices) > 0):
            self.lp = 0.67 * self.lp + 0.33 * opponent_previous_choices[-1]
        if (self.lp > 0.68):
            return 1
        else:
            return 0
    def __init__(self, pid=0):
        self.name = "eric"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)
        self.lp = 0;