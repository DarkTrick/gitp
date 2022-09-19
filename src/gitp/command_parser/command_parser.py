from typing import List, Dict, Tuple

from command_parser.dict_tree.dict_tree_finder import dictTree_find
from command_parser.command2 import Command2


def _divideMetaCommands(commandList: list[str])-> tuple[list[str]]:
  """
    Divides a command array in meta commands and
     general commands
  """

  if (len(commandList) <= 0):
    return ([],[])

  metaCommandsEndIndex = len(commandList)
  for i in range(len(commandList)):
    strCommand = commandList[i]
    if("--" != strCommand[:2]):
      metaCommandsEndIndex = i
      break

  metaCommands = commandList[:metaCommandsEndIndex]
  commands = commandList[metaCommandsEndIndex:]

  return (metaCommands, commands)


def parse(dictTree: Dict, commands: List) -> Command2:

  (metaCommands, commands) = _divideMetaCommands(commands)

  result = dictTree_find(dictTree, commands)

  cmdPath = result.nodeStack
  cmdPath.append (result.resultNode)

  return Command2(result)

