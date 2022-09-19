from testcasex.testcasex import TestCaseX
from command_parser.command_parser import parse, _divideMetaCommands


class DivideMetaCommandsTest(TestCaseX):
  def test_emptyArray(self):
    (meta, normal) = _divideMetaCommands ([])
    self.expect (len(meta)).toBe (0)
    self.expect (len(normal)).toBe (0)

  def test_oneMetaCommand(self):
    (meta, normal) = _divideMetaCommands (["--help"])
    self.expect (len(meta)).toBe (1)
    self.expect (meta[0]).toBe ("--help")
    self.expect (len(normal)).toBe (0)

  def test_oneNormalCommand(self):
    (meta, normal) = _divideMetaCommands (["aa"])
    self.expect (len(meta)).toBe (0)
    self.expect (len(normal)).toBe (1)
    self.expect (normal[0]).toBe ("aa")

  def test_metaAndNormalCOmmand(self):
    (meta, normal) = _divideMetaCommands (["--help", "aa"])
    self.expect (len(meta)).toBe (1)
    self.expect (meta[0]).toBe ("--help")
    self.expect (len(normal)).toBe (1)
    self.expect (normal[0]).toBe ("aa")

class CommandParserTest_Help(TestCaseX):

  def test_rootDescription_empty(self):
    input = {}
    result = parse(input,["--help"])
    self.expect (result.getText()).toBe ("")

  def test_rootDescription(self):
    input = {
      "__description": ["a"]
    }
    result = parse(input,["--help"])
    self.expect (result.getText()).toBe ("a")

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
