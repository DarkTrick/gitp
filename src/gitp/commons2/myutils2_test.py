import sys
print()
print()
print(sys.path)
print()
print()

import unittest
from commons2.myutils2 import coolFunction2

class Foo(unittest.TestCase):
  def test_aa(self):
    self.assertTrue(True)