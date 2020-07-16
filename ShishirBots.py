import numpy as np


class TatForTit:
    def evaluate_round(self,opponent_previous_choices):
        if(len(opponent_previous_choices)==0):
            return 1
        else:
            rand = np.random.rand()
            if(opponent_previous_choices[-1] ==0):
                if(rand<=0.1):
                    return 1
                else:
                    return 0
            elif(opponent_previous_choices[-1]==1):
                if(len(opponent_previous_choices)>6):
                    if(np.sum(opponent_previous_choices[-6:-1])==5):
                        return 1
                if(rand<=0.1):
                    return 0
                else:
                    return 1
    def __init__(self,pid):
        self.name = "tat-for-tit"
        if(pid>0):
            self.name=self.name+"-"+str(pid)
            
        
class GTT:
    def evaluate_round(self,opponent_previous_choices):
        if(len(opponent_previous_choices)==0):
            return 0
        else:
            rand = np.random.rand()
            if(opponent_previous_choices[-1] ==0):
                    return 0
            elif(opponent_previous_choices[-1]==1):
                if(rand<=0.1):
                    return 0
                else:
                    return 1
    def __init__(self,pid):
        self.name = "GTT"
        if(pid>0):
            self.name=self.name+"-"+str(pid)
            

