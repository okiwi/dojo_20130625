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
        
           
if __name__ == "__main__":
    unittest.main()
    
    
    
