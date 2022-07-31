from typing import Dict, List
from commons.errorable import Errorable
from command_parser.command import Command
from command_parser.dict_tree_finder import dictTree_find

def assembleCommand(commandDB: Dict, command: List[str]) -> Errorable:
  """
  @return: Errorable<string | None, string>
  """
  ret = Errorable()

  result = dictTree_find(commandDB, command)

  if(result == None):
    ret.error = "Command not found"
    return ret

  retCommand = Command.fromDict(result)

  if (not retCommand.isExecutable()):
    ret.error = "Command not found"
    return ret

  ret.value = retCommand
  return ret


