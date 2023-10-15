#!/usr/bin/python3

from calculator import Calc
import unittest

class TestCalc(unittest.TestCase):

	def test_minus(self):
		calc = Calc()
		result = calc.minus(4, 2)
		self.assertEqual(result, 2)

unittest.main()
