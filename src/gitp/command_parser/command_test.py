import unittest

from command_parser.command import Command

class fromDictTest(unittest.TestCase):
  def test_emptyDict(self):
    # setup
    input = {}

    # run
    actual = Command.fromDict(input)

    # check
    self.assertEqual(actual.commands, [])
    self.assertEqual(actual.description, [])
    self.assertEqual(actual.commandDescription, [])
    self.assertEqual(actual.constraints, [])
    self.assertEqual(actual.approve, None)


  def test_unrecognizedValue(self):
    # setup
    input = {"unused": ["a"]}

    # run
    actual = Command.fromDict(input)

    # check
    self.assertEqual(actual.commands, [])
    self.assertEqual(actual.description, [])
    self.assertEqual(actual.commandDescription, [])
    self.assertEqual(actual.constraints, [])
    self.assertEqual(actual.approve, None)


  def test_cmd(self):
    # setup
    input = {"__cmd": ["a"]}

    # run
    actual = Command.fromDict(input)

    # check
    expected = ["a"]
    self.assertEqual(actual.commands, expected)

    # TODO!TEST ARCHITECTURE:
    # how would I repeat the tests from test_emptyDict
    # with the current test instead of actual.command-test
    # in test_emptyDict .. like overwriting a specific
    # assert statement


  def test_desc(self):
    # setup
    input = {"__description": ["a"]}

    # run
    actual = Command.fromDict(input)

    # check
    expected = ["a"]
    self.assertEqual(actual.description, expected)


  def test_cmddesc(self):
    # setup
    input = {"__cmddescription": ["a"]}

    # run
    actual = Command.fromDict(input)

    # check
    expected = ["a"]
    self.assertEqual(actual.commandDescription, expected)


  def test_constraints(self):
    # setup
    input = {"__constraints": ["a"]}

    # run
    actual = Command.fromDict(input)

    # check
    expected = ["a"]
    self.assertEqual(actual.constraints, expected)

class isExecutable(unittest.TestCase):
  def test_True(self):
    # setup
    subject = Command()
    subject.commands = ["a"]

    # run
    actual = subject.isExecutable()

    # check
    self.assertTrue(actual)

  def test_False(self):
    # setup
    subject = Command()

    # run
    actual = subject.isExecutable()

    # check
    self.assertFalse(actual)
