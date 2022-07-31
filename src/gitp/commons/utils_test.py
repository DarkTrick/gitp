import unittest

from commons.utils import isArray


class isArrayTest(unittest.TestCase):
  def test_False(self):
    self.assertFalse (isArray("a"), "string")
    self.assertFalse (isArray(1), "int")
    self.assertFalse (isArray(None), "None")
    self.assertFalse (isArray(()), "tuple")
    self.assertFalse (isArray({}), "dictionary")

  def test_True(self):
    self.assertTrue (isArray([]), "empty array")
    self.assertTrue (isArray([[]]), "empty array of empty array")
    self.assertTrue (isArray(["a"]), "filled array")
