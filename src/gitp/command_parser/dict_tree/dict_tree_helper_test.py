from testcasex.testcasex import TestCaseX
from command_parser.dict_tree.dict_tree_helper import Node

class DictTreeNodeTest(TestCaseX):


  def test_isVariable(self):

    # All test cases to test [INPUT, EXPECTED]
    testData = [
      ["${1}", True],
      ["${2}", True],
      ["${ 1}", True],
      ["${asdf}", True],
      ["${a b c d}", True],
      ["${}", True],

      ["", False],
      [" ${1}", False],
      [" ${1", False],
      [" $1}", False],
      ["$ {1}", False],

    ]

    for testDatum in testData:
      # run
      result = Node.isVariable(testDatum[0])

      # check
      self.expect(result).toBe(testDatum[1])