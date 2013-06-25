import unittest
from Bowling import Bowling

class BolwingTests(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_can_bowl_2_times_4_equals_8(self):
        game = Bowling()
        game.roll(4)
        game.roll(4)
        self.assertEquals(8, game.score())
        
    def test_can_bowl_a_strike(self):
        game = Bowling()
        game.roll(10)
        game.roll(4)
        game.roll(4)
        self.assertEquals(26, game.score()) 
        
    def test_can_bowl_a_spare(self):
        game = Bowling()
        game.roll(6)
        game.roll(4)
        game.roll(1)
        self.assertEquals(12, game.score()) 
           
if __name__ == "__main__":
    unittest.main()
    
    
    
