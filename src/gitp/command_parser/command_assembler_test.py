import unittest
from command_parser.command_assembler import assembleCommand

class CommandAssemblerTest(unittest.TestCase):


  def test_command_not_found(self):
    # setup
    cmdDB = {}
    input = ["asdf"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    self.assertTrue(actual.failed())



  def test_command_found(self):
    # setup
    cmdDB = {"existingCommand": {"__cmd": ["foo"]}}
    input = ["existingCommand"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    with self.subTest("Correct status?"):
      self.assertTrue(actual.succeeded())

    with self.subTest("Correct type?"):
      self.assertTrue(actual != None)

    with self.subTest("Correct content?"):
     self.assertEqual(len(actual.value.commands), 1)
     self.assertEqual(actual.value.commands[0], "foo")


  def test_multiple_commands(self):
    # setup
    cmdDB = {"existingCommand":
              {"__cmd":
                ["git branch", "git merge"]
              }
            }

    input = ["existingCommand"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    self.assertEqual(actual.value.commands[0], "git branch")
    self.assertEqual(actual.value.commands[1], "git merge")




  def test_path_with_no_command(self):
    # setup
    cmdDB = {"existingCommand": {"a": "a"}}
    input = ["existingCommand"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    self.assertTrue(actual.failed())


class AssembleCommandWithVariablesTest(unittest.TestCase):

  def test_oneLevel_oneVariable(self):
    # setup
    cmdDB = {"${1}": {"__cmd": ["${1}"]}}
    input = ["a"]

    # run
    actual = assembleCommand(cmdDB, input)

    # check
    self.assertEqual(actual.value.commands[0], "a")

  def test_oneLevel_oneVariable(self):
    # setup
    cmdDB = {"${1}": {"__cmd": ["foo ${1}"]}}
    input = ["a"]

    # run
    actual = assembleCommand(cmdDB, input)

    # check
    self.assertEqual(actual.value.commands[0], "foo a")


  def test_secondLevel(self):
    # setup
    cmdDB = {"blub":
              {"${1}":
                {"__cmd": ["foo ${1}"]}
              }
            }
    input = ["blub", "a"]

    # run
    actual = assembleCommand(cmdDB, input)

    # check
    self.assertEqual(actual.value.commands[0], "foo a")

  def test_twoVariable(self):
    # setup
    cmdDB = {
              "${1}": {
                "${2}": {"__cmd": ["foo ${1} ${2}"]}
              }
            }
    input = ["a", "b"]

    # run
    actual = assembleCommand(cmdDB, input)

    # check
    self.assertEqual(actual.value.commands[0], "foo a b")


  def test_overlap_UseNonVariable(self):
    # setup
    cmdDB = {
              "${1}":  {"__cmd": ["var"]},
              "a":     {"__cmd": ["b"]}
            }
    input = ["a"]

    # run
    actual = assembleCommand(cmdDB, input)

    # check
    self.assertEqual(actual.value.commands[0], "b")

