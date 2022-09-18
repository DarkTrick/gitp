import unittest


class _ActualTestValue:
  """
    Every operation that is carried out on an expected result
    is implemented here
  """
  def __init__(self, testcase: unittest.TestCase):
    self.actualValue = None
    self.testcase = testcase

  def toBe(self, expectedValue, msg = None):
    self.testcase.assertEqual (self.actualValue, expectedValue, msg)

  def toNotBe(self, expectedValue, msg = None):
    self.testcase.assertFalse (self.actualValue == expectedValue, msg)

  def toContain(self, expectedValue, msg = None):
    self.testcase.assertTrue (expectedValue in self.actualValue, msg)


class TestCaseX(unittest.TestCase):
  """
  Extends Unittest.Testcase by `expect` function
  """

  def expect(self, value) -> _ActualTestValue:
    actValue = _ActualTestValue(self)
    actValue.actualValue = value
    return actValue