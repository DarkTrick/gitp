import unittest
from command_parser.dict_tree_finder.dict_tree_finder import dictTree_find

# TODO: move to distinct location

class DictTreeFind(unittest.TestCase):

  def test_emptyTree_emptyPath(self):
    # setup
    dictTree = {}

    # run
    actual = dictTree_find(dictTree, []).branch

    # check
    self.assertEqual(actual, dictTree)



  def test_emptyTree_pathNotFound(self):
    # setup
    dictTree = {}

    # run
    actual = dictTree_find (dictTree, ["a"]).branch

    # check
    self.assertEqual (actual, None)


class DictTreeFind_MultipleLevels(unittest.TestCase):

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
    res = dictTree_find (self.dictTree, ["1","1.1","1.1.1"])
    actual = res.branch

    # check
    self.assertEqual (actual, None)


  def test_B(self):
    # run
    res = dictTree_find (self.dictTree, ["2","2.1"])
    actual = res.branch["v"]

    # check
    self.assertEqual (actual, "b.a")

  def test_C(self):
    # run
    res = dictTree_find (self.dictTree, ["2","2.3", "2.3.2"])
    actual = res.branch["v"]

    # check
    self.assertEqual (actual, "b.c.b")

  def test_D(self):
    # run
    res = dictTree_find (self.dictTree, ["3"])
    actual = res.branch

    # check
    self.assertEqual (actual, None)


  def check(self, searchPath, expected):
    # run
    res = dictTree_find (self.dictTree, searchPath)
    actual = res.branch

    # check
    self.assertEqual (actual, expected)



class DictTreeFind_MemorizeVariables(unittest.TestCase):
  def test_oneVariable(self):
    # setup
    dictTree = {"${1}": {"v": "a"}}
    searchPath = ["a"]

    # run
    res = dictTree_find (dictTree, searchPath)
    actual = res.variableDictionary

    # check
    self.assertTrue ("${1}" in actual)
    self.assertEqual(actual["${1}"], "a")

  def test_twoVariable(self):
    # setup
    dictTree = {"${1}": {"${2}": {"v": "a"}}}
    searchPath = ["a", "b"]

    # run
    res = dictTree_find (dictTree, searchPath)
    actual = res.variableDictionary

    # check
    self.assertTrue ("${2}" in actual)
    self.assertEqual(actual["${2}"], "b")