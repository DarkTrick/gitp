

from typing import List, Dict

class DictTreeFindResult:
  def __init__(self):
    self.branch: Dict | None = {}
    self.variableDictionary: Dict = {}

    """途中で見つけたノードを保管すする"""
    self.nodeStack: list[dict] = []


def dictTree_find(dictTree: Dict, searchPath: List) -> DictTreeFindResult:
  """
  Search `searchPath` in dictTree

  @return: success: dict_tree
           fail: None
  """
  result = DictTreeFindResult()
  return _dictTree_find(dictTree, searchPath, result)



def _dictTree_find(dictTree: Dict, searchPath: List[str], result: DictTreeFindResult) -> DictTreeFindResult:
  def isVariable(string):
    return branchKey[:2] == "${" and branchKey[-1] == "}"

  if(searchPath == []):
    result.branch = dictTree
    return result

  # find `key` in `dictTree`
  searchKey = searchPath[0]
  if(searchKey in dictTree):
    newTree = dictTree[searchKey]
    newSearchPath = searchPath[1:]

    if(not isinstance(newTree, dict)):
      result.branch = None
      return result

    return _dictTree_find(newTree, newSearchPath, result)


  # check, if the next branch is a variable
  for branchKey, branch in dictTree.items():
    if(isVariable(branchKey)):
      result.variableDictionary[branchKey] = searchKey
      result.branch = branch
      newTree = dictTree[branchKey]
      newSearchPath = searchPath[1:]
      return _dictTree_find(newTree, newSearchPath, result)

  # not match found, so reaturn None
  result.branch = None
  return result