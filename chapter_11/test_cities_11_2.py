import unittest
from city_functions_11_2 import city_country


class testing_city_country_function(unittest.TestCase):
    """this is the class to test the function city_country()"""

    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")
    pass

    def test_city_country_population(self):
        result = city_country('santiago', 'chile', 5000000)
        self.assertEqual(result, 'Santiago, Chile - population 5000000.')
    pass


if __name__ == '__main__':
    unittest.main()
