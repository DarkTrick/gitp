from testcasex.testcasex import TestCaseX
from command_parser.command_parser import parse

class CommandParserTest_Help(TestCaseX):

  def test_rootDescription_empty(self):
    input = {}
    result = parse(input,["--help"])
    self.expect (result.getText()).toBe ("")

  #def test_rootDescription(self):
  #  input = {
  #    "__description": ["a"]
  #  }
  #  result = parse(input,["--help"])
  #  self.expect (result.getText()).toBe ("a")

  # TODO1: FIRST SOLVE ABOVE
  #def test_subCommands(self):
  #  input = {
  #    "__description": "desc root",
  #    "a": {
  #      "__description": "desc a"
  #    },
  #    "b": {
  #      "__description": "desc b"
  #    }
  #  }
  #  result = parse (input, ["--help"])
  #  self.expect (result.getTextOutput ()). toBe ("")
