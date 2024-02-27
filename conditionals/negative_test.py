import unittest
from return_negative import make_negative

class TestNegativeNumber(unittest.TestCase):
  def test_negative_number(self):
    data = 10
    result = make_negative(data)
    self.assertEqual(-10, result)

  def test_negative_number_2(self):
    data = 0
    result = make_negative(data)
    self.assertEqual(0,result)

if __name__ == '__main__':
  unittest.main()
