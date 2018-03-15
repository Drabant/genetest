import unittest

from object import *

class TestMale(unittest.TestCase):
    def test(self):
        self.assertEqual(Human(gender=MALE), MALE)

class TestFemale(unittest.TestCase):
    def test(self):
        self.assertEqual(Human(gender=FEMALE), MALE)
