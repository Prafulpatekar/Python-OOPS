from calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add_numbers_return_sum(self):
        result = self.calculator.add(5,8)
        self.assertEqual(5+8,result)

        result = self.calculator.add(5.22,8)
        self.assertEqual(5.22+8,result)

        result = self.calculator.add(55,8.02)
        self.assertEqual(55+8.02,result)

        result = self.calculator.add(5.5,8.02)
        self.assertEqual(5.5+8.02,result)

    def test_add_non_numbers_rasie_type_error(self):
        self.assertRaises(TypeError,self.calculator.add,"HELLOW","NUMBER")
        self.assertRaises(TypeError,self.calculator.add,5,"NUMBER")
        self.assertRaises(TypeError,self.calculator.add,"HSHWWH",56)
        self.assertRaises(TypeError,self.calculator.add,"123.23.32.2",56)

    def test_add_string_numbers_return_sum(self):
        self.assertEqual(60+50,self.calculator.add("60","50"))
        self.assertEqual(60+50,self.calculator.add(60,"50"))
        self.assertEqual(60+50,self.calculator.add("60",50))
        self.assertEqual(6.50+5.50,self.calculator.add("6.50","5.50"))
        self.assertEqual(6.50+5.50,self.calculator.add("6.50",5.50))
        self.assertEqual(6.50+5.50,self.calculator.add(6.50,"5.50"))

    def test_add_negative_numbers_return_sum(self):
        self.assertEqual(-60-50,self.calculator.add("-60","-50"))
        self.assertEqual(60-50,self.calculator.add(60,"-50"))
        self.assertEqual(-60+50,self.calculator.add("-60",50))
        self.assertEqual(-6.50-5.50,self.calculator.add("-6.50","-5.50"))
        self.assertEqual(-6.50+5.50,self.calculator.add("-6.50",5.50))
        self.assertEqual(6.50-5.50,self.calculator.add(6.50,"-5.50"))