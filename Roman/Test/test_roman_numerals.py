import unittest
from src.roman_numbers_conversion import RomanDecimalConversion

class RomanDecimalTest(unittest.TestCase):
    def createInstance(self):
        #creates a new instance of the class
        self.new_conversion = RomanDecimalConversion()

    def test_one_conversion(self):
        self.assertEquals(self.new_conversion.convert(1), "I")

    def test_two_conversion(self):
        self.assertEquals(self.new_conversion.convert(2), "II")

    def test_five_conversion(self):
        self.assertEquals(self.new_conversion.convert(5), "V")

    def test_six_conversion(self):
        self.assertEquals(self.new_conversion.convert(6), "VI")

    def test_four_conversion(self):
        self.assertEquals(self.new_conversion.convert(4), "IV")

    def test_ten_conversion(self):
        self.assertEquals(self.new_conversion.convert(10), "X")

    def test_nine_conversion(self):
        self.assertEquals(self.new_conversion.convert(9), "IX")

if __name__ == '__main__':
    unittest.main()
