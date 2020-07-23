import numpy as np

class HotStartOpportunist:
    
    def evaluate_round(self, opponent_previous_choices):   
        # Set the number of turns to remember
        # (timeout before I strike)
        n_rounds_memory = int(3)

        # If this is the first round, I always defect
        if   (len(opponent_previous_choices) == 0):
            return 1
        
        # For the next few rounds, I do what opponent did last round
        elif(len(opponent_previous_choices) < n_rounds_memory):
            return opponent_previous_choices[-1]
        
        # After first few rounds, if there are some number of rounds without a strike, I defect
        else:
            recent_opp_choices = opponent_previous_choices[-(1+n_rounds_memory):-1]
            no_recent_strike = (np.sum(recent_opp_choices) == 0)
            # If the opponent hasn't defected in a while, I defect
            if (no_recent_strike):
                return 1
            # If they have defected recently, I do what they did
            else:
                return opponent_previous_choices[-1]
    
    def __init__(self, pid=0):
        self.name = "hot-start-opportunist"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)
        
class HotStartCooperatorWithGrudge:
    
    def evaluate_round(self, opponent_previous_choices):
        # Grudge fogiveness probability
        # Larger forgiveness factors are shorter grudges
        p_forgive = 0.10        # i.e., forgiveness in 10 rounds

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
                    
            # For every turn since last time opponent defected, probability I defect drops
            p_defect = np.min([0., 1.- p_forgive*nturns_since_defect])
            
            # Given that probability, decide if I defect
            rando = np.random.rand()
            if (rando < p_defect):
                return 1 # I defect
            else:
                return 0 # I don't
                 
    def __init__(self, pid=0):
        self.name = "hot-start-cooperator-with-a-grudge"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)

class RetalitoryCooperator:
    
    def evaluate_round(self, opponent_previous_choices):
        # Grudge fogiveness probability
        # Larger forgiveness factors are shorter grudges
        p_forgive = 0.20        # i.e., forgiveness in 5 rounds

        # If this is the first round, I always remain
        if   (len(opponent_previous_choices) == 0):
            return 0
        
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
                    
            # For every turn since last time opponent defected, probability I defect drops
            p_defect = np.min([0., 1.- p_forgive*nturns_since_defect])
            
            # Given that probability, decide if I defect
            rando = np.random.rand()
            if (rando < p_defect):
                return 1 # I defect
            else:
                return 0 # I don't
                 
    def __init__(self, pid=0):
        self.name = "retalitory-cooperator"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)

class BiasedStatisticalStriker:
    
    def evaluate_round(self, opponent_previous_choices):
        # Set the number of turns to remember
        # (timeout before algorithm takes over)
        n_rounds_memory = int(8)

        # How angry are you at your opponent?
        # Higher bias factors mean more likely to respond with a strike
        # Lower  bias factors mean lower probability of retaliating with a strike
        # 1.0 is neutral
        bias_factor = 0.5
        bias_factor = 1.0 if (bias_factor <= 0) else bias_factor

        # If this is the first round, I always remain
        if   (len(opponent_previous_choices) == 0):
            return 0

        # In the next few rounds do what opponent did prior
        if   (len(opponent_previous_choices) < n_rounds_memory):
            return opponent_previous_choices[-1]
        
        # Once we're n_rounds_memory into the game
        else:
            # Count how many times opponent has defected in memory
            n_opp_strike = np.sum(opponent_previous_choices[-n_rounds_memory:])

            # Fraction of memory that were strikes
            f_opp_strike = n_opp_strike / float(n_rounds_memory)

            # Respond with a strike based on their fraction
            rando = np.random.rand()
            randp = rando / bias_factor
            if (randp < f_opp_strike):
                return 1 # I defect
            else:
                return 0 # I don't
        
                 
    def __init__(self, pid=0):
        self.name = "biased-statistical-striker"
        if (pid > 0):
            self.name = self.name+"-"+str(pid)