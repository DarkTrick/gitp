

from typing import List, Dict

from command_parser.dict_tree.dict_tree_helper_test import Node

class DictTreeFindResult:
  def __init__(self):
    self.resultNode: Dict | None = None
    self.variableDictionary: Dict = {}

    """
      Stores the path taken, excluding variable nodes and leafs
    """
    self.nodeStack: list[Dict] = []


  def foundPath(self):
    return self.resultNode != None


def dictTree_find(dictTree: Dict, searchPath: List) -> DictTreeFindResult:
  """
  Search `searchPath` in dictTree

  @return: success: dict_tree
           fail: None
  """
  result = DictTreeFindResult()
  return _dictTree_find(dictTree, searchPath, result)



def _dictTree_find(dictTree: Dict, searchPath: List[str], result: DictTreeFindResult, isVariable = False) -> DictTreeFindResult:

  if(False == isVariable):
    result.nodeStack.append (dictTree)

  # successfully finish searching
  if(searchPath == []):
    result.resultNode = dictTree
    return result

  # find `key` in `dictTree`
  searchKey = searchPath[0]
  if(searchKey in dictTree):
    newTree = dictTree[searchKey]
    newSearchPath = searchPath[1:]

    if(not isinstance(newTree, dict)):
      return result

    return _dictTree_find(newTree, newSearchPath, result)


  # check, if the next branch has a variable key
  for nodeKey, node in dictTree.items():
    if(Node.isVariable(nodeKey)):
      result.variableDictionary[nodeKey] = searchKey
      newTree = dictTree[nodeKey]
      newSearchPath = searchPath[1:]
      return _dictTree_find(newTree, newSearchPath, result, True)

  # no match found
  return result