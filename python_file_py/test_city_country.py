import unittest
from function_city_describe import city_country as city


class CityTestCase(unittest.TestCase):
    """用chongqing和china测试city_country"""
    def test_city_country(self):
        country = city('chongqing', 'china', 1000_0000)
        self.assertEqual(country, 'Chongqing, China ---population 10000000.')


if __name__ == '__main__':
    unittest.main()