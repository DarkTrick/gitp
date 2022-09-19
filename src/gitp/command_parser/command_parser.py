from typing import List, Dict

from command_parser.dict_tree.dict_tree_finder import dictTree_find
from command_parser.command2 import Command2




def parse(dictTree: Dict, commands: List) -> Command2:

  # find end of meta commands (meta command = --help, --explain, ...)
  metaCommandsEndIndex = 0
  for i in range(len(commands)):
    strCommand = commands[i]
    if("--" != strCommand[:2]):
      metaCommandsEndIndex = i
      break

  strMetaCommands = commands[:metaCommandsEndIndex]
  strCommands = [metaCommandsEndIndex]

  result = dictTree_find(dictTree, strCommands)

  cmdPath = result.nodeStack
  cmdPath.append (result.resultNode)

  return Command2(strCommands, cmdPath, strMetaCommands)

