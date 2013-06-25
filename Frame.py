class Frame (object):
    
    def __init__(self):
        self.bowls = []
        self.is_strike = False
        self.next_frame = None
        self.is_spare = False
        
    def add_bowl(self, pins):
        self.bowls.append(pins)
        
        if len(self.bowls) == 1 and pins == 10:
            self.is_strike = True
        if len(self.bowls) == 2 and self.get_bowl_total() == 10:
            self.is_spare = True
        
    def get_bowl_total(self):
        score_frame = 0
        
        for bowl in self.bowls:
            score_frame += bowl
       
        return score_frame

    def get_score(self):
        score = self.get_bowl_total()
 
        if self.is_spare and self.next_frame:
            score += self.next_frame.bowls[0]
        if self.is_strike and self.next_frame:
            score += 2 * self.next_frame.get_bowl_total()
        return score

 
        
        
        
        
