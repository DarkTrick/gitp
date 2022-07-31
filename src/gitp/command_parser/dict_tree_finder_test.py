import unittest
from command_parser.dict_tree_finder import dictTree_find

# TODO: move to distinct location

class DictTreeFind(unittest.TestCase):

  def test_emptyTree_emptyPath(self):
    # setup
    dictTree = {}

    # run
    actual = dictTree_find(dictTree, [])

    # check
    self.assertEqual(actual, dictTree)



  def test_emptyTree_pathNotFound(self):
    # setup
    dictTree = {}

    # run
    actual = dictTree_find (dictTree, ["a"])

    # check
    self.assertEqual (actual, None)


class DictTreeFind_MultipleLevels(unittest.TestCase):

  def setUp(self):
    self.dictTree = {
      "1": {
        "1.1": "a.a",
        "1.2": "a.b",
      },
      "2": {
        "2.1": "b.a",
        "2.2": "b.b",
        "2.3": {
          "2.3.1": "b.c.a",
          "2.3.2": "b.c.b",
          "2.3.3": "b.c.c",
        }
      }
    }

  def test_A(self): self.check(["1","1.1","1.1.1"], None)
  def test_B(self): self.check(["2","2.1"], "b.a")
  def test_C(self): self.check(["2","2.3", "2.3.2"], "b.c.b")
  def test_D(self): self.check(["3"], None)


  def check(self, searchPath, expected):
    # run
    actual = dictTree_find (self.dictTree, searchPath)

    # check
    self.assertEqual (actual, expected)

