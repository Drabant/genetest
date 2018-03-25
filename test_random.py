import unittest

import dnd

class TestDiceSpread(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.testsize = 100000
        self.accept = .05

        dicerolls = {}
        for i in range(0,self.testsize):
            roll = dnd.Character().a_str
            if roll in dicerolls:
                dicerolls[roll] += 1
            else:
                dicerolls[roll] = 1
        self.dicerolls = dicerolls

    def test_18_result(self):
        chance = 1/216

        self.assertLess(self.dicerolls[18], chance * self.testsize * (1+self.accept))
        self.assertGreater(self.dicerolls[18], chance * self.testsize * (1-self.accept))

    def test_3_result(self):
        chance = 1/216

        self.assertLess(self.dicerolls[3], chance * self.testsize * (1+self.accept))
        self.assertGreater(self.dicerolls[3], chance * self.testsize * (1-self.accept))



if __name__ =='__main__':
    unittest.main()
