import unittest

from commons.utils import isArray, string_replaceWithDict


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


class String_replaceWithDictTest(unittest.TestCase):
  def test_noReplacement(self):
    # setup
    input = "zz"
    replaceDict = {"a": "b"}
    expected = input

    # run
    actual = string_replaceWithDict(input,replaceDict)

    # check
    self.assertEqual(actual, expected)

  def test_a(self):
    # setup
    replaceDict = {
      "a": "b",
      "c": "d"
    }

    # run
    actual = string_replaceWithDict("aacc",replaceDict)

    # check
    self.assertEqual(actual, "bbdd")