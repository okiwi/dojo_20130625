from Frame import Frame
class Bowling (object):
    
    def __init__(self):
        self.frame = Frame()
        self.frames = []
    
    def roll(self, pins):
        current_score = 0
        if len(self.frame.bowls) == 2:
            next_frame = Frame()
            self.frame.next_frame = next_frame
            self.frames.append(self.frame)
            self.frame = next_frame
        
        self.frame.add_bowl(pins)
        
    def score(self):
        score = 0
        
        for frame in self.frames:
            score += frame.get_score()
            
        score += self.frame.get_bowl_total()
        
        return score
        

