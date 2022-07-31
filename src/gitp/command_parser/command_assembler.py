from typing import Dict, List
from commons.errorable import Errorable
from command_parser.command import Command
from command_parser.dict_tree_finder import dictTree_find


def assembleCommand(commandDB: Dict, commandInput: List[str]) -> Errorable:
  """
  @return: Errorable<Command>
  """
  ret = Errorable()

  result = dictTree_find(commandDB, commandInput)

  if(result.branch == None):
    ret.error = "Command not found"
    return ret

  command = Command.fromDict(result.branch, result.variableDictionary)

  if (not command.isExecutable()):
    ret.error = "Command not found"
    return ret

  ret.value = command
  return ret


