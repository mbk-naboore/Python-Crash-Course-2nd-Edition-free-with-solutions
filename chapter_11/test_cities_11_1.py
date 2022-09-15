import unittest
from city_functions_11_1 import city_country


class testing_city_country_function(unittest.TestCase):
    """this is the class to test the function city_country()"""

    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")
    pass


if __name__ == '__main__':
    unittest.main()
