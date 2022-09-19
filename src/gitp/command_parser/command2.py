from typing import List, Dict


# TODO: replace current `Command` with `Command2` here
class Command2:
  def __init__(self, strCommands: list[str], treePath: list[Dict], metaCommand: list[str]):
    """
      @param treePath:
          If last item is None
    """
    #self.treePath: list[Dict] = treePath
    #self.strCommands: list[str] = strCommands
    #self.metaCommands: list[str] = metaCommand

  def formatDescription(self):
    return ""

  def getText(self):
    return ""
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