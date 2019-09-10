import unittest
import os

from sum import series_sum


class TestSum(unittest.TestCase):
	def test_area(self):
		self.assertEqual(series_sum(1), "1.00")
		# self.assertEqual(series_sum(2), "2.25")
		# self.assertEqual(series_sum(2), "1.39")


if __name__ == '__main__':
	unittest.main()