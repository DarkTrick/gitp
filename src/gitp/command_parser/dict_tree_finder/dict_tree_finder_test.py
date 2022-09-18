import unittest
from testcasex.testcasex import TestCaseX
from command_parser.dict_tree_finder.dict_tree_finder import dictTree_find




class DictTreeFind(TestCaseX):

  def test_emptyTree_emptyPath(self):
    # setup
    dictTree = {}

    # run
    result = dictTree_find(dictTree, [])

    # check
    self.expect (result.branch).toBe (dictTree)



  def test_emptyTree_pathNotFound(self):
    # setup
    dictTree = {}

    # run
    result = dictTree_find (dictTree, ["a"])

    # check
    self.expect (result.branch).toBe (None)



class DictTreeFind_MultipleLevels(TestCaseX):

  def setUp(self):
    self.dictTree = {
      "1": {
        "1.1": {"v": "a.a"},
        "1.2": {"v": "a.b"},
      },
      "2": {
        "2.1": {"v": "b.a"},
        "2.2": {"v": "b.b"},
        "2.3": {
          "2.3.1": {"v": "b.c.a"},
          "2.3.2": {"v": "b.c.b"},
          "2.3.3": {"v": "b.c.c"},
        }
      }
    }

  def test_A(self):
    # run
    input = ["1","1.1","1.1.1"]
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect (result.branch).toBe (None)

  def test_B(self):
    # run
    input = ["2","2.1"]
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect (result.branch["v"]).toBe ("b.a")

  def test_C(self):
    # run
    input = ["2","2.3", "2.3.2"]
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect (result.branch["v"]).toBe ("b.c.b")

  def test_D(self):
    # run
    input = ["3"]
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect (result.branch).toBe (None)


  def check(self, searchPath, expected):
    # run
    input = searchPath
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect (result.branch).toBe (expected)


class DictTreeFindTest_NodeLevels(TestCaseX):

  def setUp(self):
    self.dictTree = {
      "1": {
        "1.1": {"v": "a.a"},
        "1.2": {"v": "a.b"},
      },
      "2": {
        "2.1": {"v": "b.a"},
        "2.2": {"v": "b.b"},
        "2.3": {
          "2.3.1": {"v": "b.c.a"},
          "2.3.2": {"v": "b.c.b"},
          "2.3.3": {"v": "b.c.c"},
        }
      },
      "${1}": {
        "a": {"v": "${1}.a"},
        "b": {"v": "${1}.b"}
      }
    }

  def test_level1(self):
    # setup
    input = ["1"]

    # run
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect(len(result.nodeStack)).toBe (2)
    self.expect(result.nodeStack[0]).toBe (self.dictTree)
    self.expect(result.nodeStack[1]).toBe (self.dictTree["1"])

  def test_level2(self):
    # setup
    input = ["2", "2.3"]

    # run
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect(len(result.nodeStack)).toBe (3)
    self.expect(result.nodeStack[0]).toBe (self.dictTree)
    self.expect(result.nodeStack[1]).toBe (self.dictTree["2"])
    self.expect(result.nodeStack[2]).toBe (self.dictTree["2"]["2.3"])

  def test_variableNode(self):
    # setup
    input = ["A", "b"]

    # run
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect(len(result.nodeStack)).toBe (2)
    self.expect(result.nodeStack[0]).toBe (self.dictTree)
    self.expect(result.nodeStack[1]).toBe (self.dictTree["${1}"]["b"])

  def test_caseNotFound(self):
    # setup
    input = ["2", "notFound"]

    # run
    result = dictTree_find (self.dictTree, input)

    # check
    self.expect(len(result.nodeStack)).toBe (2)
    self.expect(result.nodeStack[0]).toBe (self.dictTree)
    self.expect(result.nodeStack[1]).toBe (self.dictTree["2"])

class DictTreeFind_MemorizeVariables(TestCaseX):
  def test_oneVariable(self):
    # setup
    dictTree = {"${1}": {"v": "a"}}
    searchPath = ["a"]

    # run
    result = dictTree_find (dictTree, searchPath)

    # check
    self.expect (result.variableDictionary).toContain("${1}")
    self.expect (result.variableDictionary["${1}"]).toBe ("a")

  def test_twoVariables(self):
    # setup
    dictTree = {"${1}": {"${2}": {"v": "a"}}}
    searchPath = ["a", "b"]

    # run
    result = dictTree_find (dictTree, searchPath)

    # check
    self.expect (result.variableDictionary).toContain("${2}")
    self.expect (result.variableDictionary["${2}"]).toBe ("b")