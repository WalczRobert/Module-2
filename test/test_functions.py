import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        age_in_years = 3
        convert_to_months =36
        self.assertEqual(convert_to_months, camper_age_input.convert_to_months(age_in_years))


if __name__ == '__main__':
    unittest.main()

#convert_to_months
#age_in_years
#age_in_months
