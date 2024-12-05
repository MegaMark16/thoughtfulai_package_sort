import unittest
from package_sorter import sort

class TestPackageSorter(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(50, 75, 100, 10), "STANDARD")

    def test_bulky_package_total_dimensions(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_bulky_package_single_dimension(self):
        self.assertEqual(sort(50, 50, 150, 10), "SPECIAL")

    def test_heavy_package(self):
        self.assertEqual(sort(20, 30, 40, 20), "SPECIAL")

    def test_very_heavy_package(self):
        self.assertEqual(sort(20, 30, 40, 2000), "SPECIAL")

    def test_bulky_and_heavy_package(self):
        self.assertEqual(sort(100, 150, 200, 25), "REJECTED")

    def test_invalid_dimensions(self):
        self.assertEqual(sort(100, 150, 200, 25), "REJECTED")

    def test_invalid_mass(self):
        self.assertEqual(sort(100, 150, 200, 25), "REJECTED")

    def test_invalid_dimension_negative(self):
        with self.assertRaises(ValueError) as context:
            sort(-10, 150, 200, 25)
        self.assertEqual(str(context.exception), "width must be a positive integer, but got '-10'")

    def test_invalid_dimension_type(self):
        with self.assertRaises(ValueError) as context:
            sort('test', 150, 200, 25)
        self.assertEqual(str(context.exception), "width must be a positive integer, but got 'test'")

    def test_invalid_mass_negative(self):
        with self.assertRaises(ValueError) as context:
            sort(100, 150, 200, 0)
        self.assertEqual(str(context.exception), "mass must be a positive integer, but got '0'")

    def test_invalid_mass_type(self):
        with self.assertRaises(ValueError) as context:
            sort(100, 150, 200, 'test')
        self.assertEqual(str(context.exception), "mass must be a positive integer, but got 'test'")

if __name__ == "__main__":
    unittest.main()