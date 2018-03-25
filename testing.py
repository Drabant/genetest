import unittest

from object import *

class TestMale(unittest.TestCase):
    def test(self):
        self.assertEqual(Human(gender=MALE).gender, MALE)

class TestFemale(unittest.TestCase):
    def test(self):
        self.assertEqual(Human(gender=FEMALE).gender, MALE)

unittest.main()
