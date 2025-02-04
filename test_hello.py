import unittest
from hello import calculate_year_of_100  # Import the function from hello.py

class TestCalculateYear(unittest.TestCase):
    def test_calculate_year(self):
        self.assertEqual(calculate_year_of_100(25), 2098)  # 2023 - 25 + 100
        self.assertEqual(calculate_year_of_100(50), 2073)
        self.assertEqual(calculate_year_of_100(100), 2023)
        self.assertEqual(calculate_year_of_100(0), 2123)
        self.assertEqual(calculate_year_of_100(75, 2050), 2075)  # Future year scenario

if __name__ == "__main__":
    unittest.main()