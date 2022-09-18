from testcasex.testcasex import TestCaseX
from command_parser.command_assembler import assembleCommand

class CommandAssemblerTest(TestCaseX):


  def test_command_not_found(self):
    # setup
    cmdDB = {}
    input = ["asdf"]

    # run
    result = assembleCommand(cmdDB,input)

    # check
    self.expect(result.failed()).toBe (True)



  def test_command_found(self):
    # setup
    cmdDB = {"existingCommand": {"__cmd": ["foo"]}}
    input = ["existingCommand"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    with self.subTest("Correct status?"):
      self.expect (actual.succeeded()).toBe (True)

    with self.subTest("Correct type?"):
      self.expect (actual).toNotBe (None)

    with self.subTest("Correct content?"):
     self.expect (len(actual.value.commands)).toBe (1)
     self.expect(actual.value.commands[0]).toBe ("foo")


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
    self.expect(actual.value.commands[0]).toBe ("git branch")
    self.expect(actual.value.commands[1]).toBe ("git merge")




  def test_path_with_no_command(self):
    # setup
    cmdDB = {"existingCommand": {"a": "a"}}
    input = ["existingCommand"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    self.assertTrue(actual.failed())


class AssembleCommandWithVariablesTest(TestCaseX):

  def test_oneLevel_oneVariable(self):
    # setup
    cmdDB = {"${1}": {"__cmd": ["${1}"]}}
    input = ["a"]

    # run
    actual = assembleCommand(cmdDB, input)

    # check
    self.expect(actual.value.commands[0]).toBe ("a")

  def test_oneLevel_oneVariable(self):
    # setup
    cmdDB = {"${1}": {"__cmd": ["foo ${1}"]}}
    input = ["a"]

    # run
    actual = assembleCommand(cmdDB, input)

    # check
    self.expect(actual.value.commands[0]).toBe ("foo a")


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
    self.expect(actual.value.commands[0]).toBe ("foo a")

  def test_twoVariables(self):
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
    self.expect(actual.value.commands[0]).toBe ("foo a b")


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
    self.expect(actual.value.commands[0]).toBe ("b")

