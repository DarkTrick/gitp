

from typing import List, Dict


def dictTree_find(dictTree: Dict, searchPath: List) -> Dict | None:
  """
  Search `searchPath` in dictTree

  @return: success: dict_tree
           fail: None
  """

  return _dictTree_find(dictTree, searchPath)



def _dictTree_find(dictTree, searchPath):
  if(searchPath == []):
    return dictTree

  key = searchPath[0]
  if(key in dictTree):
    return _dictTree_find(dictTree[key], searchPath[1:])

  return None