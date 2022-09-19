from typing import List, Dict

from command_parser.dict_tree.dict_tree_finder import DictTreeFindResult
from commons.utils import dict_get, strArray_toString


DESC = "__description"
CMDDESC = "__cmddescription"
RUN = "__run"


# TODO: replace current `Command` with `Command2` here
class Command2:
  def __init__(self, dictTreeFindResult: DictTreeFindResult):
    """
      @param treePath:
          If last item is None
    """
    self.dictTreeInfo = dictTreeFindResult
    #self.treePath: list[Dict] = treePath
    #self.strCommands: list[str] = strCommands
    #self.metaCommands: list[str] = metaCommand

  def formatDescription(self):
    return ""

  def getText(self):
    arrDescription = dict_get(self.dictTreeInfo.resultNode,DESC,"")
    description = strArray_toString (arrDescription)

    return description
    #if (len (self.metaCommands) <= 0):
    #  return ""
    #
    #strCmd = self.metaCommands[0]
    ## For now: ignore the rest
    #
    #if (strCmd == "--help"):
    #  if(not "__description" in self.treeNode):
    #    return
    #  desc = self.treeNode[]
    #  "\n".join()
    #  return str(self.treeNode["__description"])

    return ""

  # TODO2: write tests
  def isExecutable(self):
    return False
    #if(not "__run" in self.treeNode):
    #    return False

    #return len(self.treeNode["__run"]) > 0

  def run(self):
    pass