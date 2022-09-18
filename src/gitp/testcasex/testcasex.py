import unittest


class _ActualTestValue:
  """
    Every operation that is carried out on an expected result
    is implemented here
  """
  def __init__(self, testcase: unittest.TestCase):
    self.actualValue = None
    self.expectedValue = None
    self.testcase = testcase

  def _formatMessage(self, msg):

    _msg = ""
    if(None != msg):
      _msg = "\n" + "   Message:  " + str(msg)

    return "\n" + "   Expected:  '" + str(self.expectedValue) + "'" + \
           "\n" + "   Actual:    '" + str(self.actualValue)   + "'" + \
            _msg

  def toBe(self, expectedValue, msg = None):
    self.expectedValue = expectedValue
    self.testcase.assertEqual (self.actualValue, expectedValue, self._formatMessage(msg))

  def toNotBe(self, expectedValue, msg = None):
    self.expectedValue = expectedValue
    self.testcase.assertFalse (self.actualValue == expectedValue, self._formatMessage(msg))

  def toContain(self, expectedValue, msg = None):
    self.expectedValue = expectedValue
    self.testcase.assertTrue (expectedValue in self.actualValue, self._formatMessage(msg))


class TestCaseX(unittest.TestCase):
  """
  Extends Unittest.Testcase by `expect` function
  """

  def expect(self, value) -> _ActualTestValue:
    actValue = _ActualTestValue(self)
    actValue.actualValue = value
    return actValue