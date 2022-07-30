import unittest
from function_formatted_tidy_name_chooseable import get_formatted_name as g


class NamesTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = g('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
	unittest.main()
