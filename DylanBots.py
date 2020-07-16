import numpy as np

class Dylan1:
    
    def evaluate_round(self, opponent_previous_choices, n_peace_pre_strike=3):   
        # If this is the first round, I always defect
        if   (len(opponent_previous_choices) == 0):
            return 1
        
        # For the next few rounds, I do what opponent did last round
        elif(len(opponent_previous_choices) < n_peace_pre_strike):
            return opponent_previous_choices[-1]
        
        # After first few rounds, if there are some number of rounds without a strike, I defect
        else:
            recent_opp_choices = opponent_previous_choices[-(1+n_peace_pre_strike):-1]
            no_recent_strike = (np.sum(recent_opp_choices) == 0)
            # If the opponent hasn't defected in a while, I defect
            if (no_recent_strike):
                return 1
            # If they have defected recently, I do what they did
            else:
                return opponent_previous_choices[-1]
    
    def __init__(self, pid=0):
        self.name = "dylan1"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)
        
class Dylan2:
    
    def evaluate_round(self, opponent_previous_choices):
        
        # If this is the first round, I always defect
        if   (len(opponent_previous_choices) == 0):
            return 1
        
        # Did the opponent defect last round?
        last_round_defect = opponent_previous_choices[-1]
        
        # If they did, I strike back
        if (last_round_defect):
            return 1
        
        # If they did not strike last round
        else:
            # Have they ever defected?
            opp_defected = (np.sum(opponent_previous_choices) > 0)
            if not opp_defected:
                return 0   # if not, I won't defect either
            
            # Count how many turns since opponent last defected
            last_defection_found = False
            nturns_since_defect  = 1
            while not last_defection_found:
                val = opponent_previous_choices[int(-1*nturns_since_defect)]
                if (val > 0):
                    last_defection_found = True
                else:
                    nturns_since_defect += 1
                    
            # For every turn since last time opponent defected, probability I defect drops by 20%
            p_defect = 1. - 0.2*nturns_since_defect
            
            # Given that probability, decide if I defect
            rando = np.random.rand()
            if (rando < p_defect):
                return 1 # I defect
            else:
                return 0 # I don't
                 
    def __init__(self, pid=0):
        self.name = "dylan2"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)