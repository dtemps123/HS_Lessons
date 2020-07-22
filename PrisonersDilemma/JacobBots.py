import time
import numpy as np
class TimeKeeper:
    def evaluate_round(self, opponent_previous_choices):
        CurrentTime = int(time.time())
        if(len(opponent_previous_choices)==0):
            Digits = np.array([int(digit) for digit in str(CurrentTime)])
            SevenCut = (Digits==7)
            HowManySevens = SevenCut.sum()
            if(HowManySevens==3):
                return 1
            else:
                return 0
        elif(opponent_previous_choices[-1]==(CurrentTime%2)):
            return opponent_previous_choices[-1]
        else:
            return 1-opponent_previous_choices[-1]
    def __init__(self, pid=0):
        self.name = "time-keeper"
        if (pid > 0): 
            self.name = self.name+"-"+str(pid)