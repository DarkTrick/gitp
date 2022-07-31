from typing import List, Dict
from commons.utils import makeArray, dict_get, string_replaceWithDict, stringArray_replaceWithDict

class Command:

  def __init__(self):
    self.commands: List = []
    self.description: List = []
    self.commandDescription: List = []
    self.constraints: List = []
    self.approve = None


  @staticmethod
  def fromDict(dict: Dict, variableDictionary: Dict = {}):

    """
    Create `Command` from a string dictionary

    @param dict:
      __cmd:
        Type: array
        Specifies the commands to be run.

      __description:
          Type: array
          Explanation shown for the command when --help was run.

      __cmddescription:
          Type: array
          Explanation of how the command works. This is shown,
          when the user shows the command of a command.

    @param variableDictionary:
      dictionary of variable values contained in dict.__cmd

    """

    def getDictArray(key) -> List:
      return makeArray(dict_get(dict, key, []))


    me = Command()
    me.commands = getDictArray ("__cmd")

    me.commands = stringArray_replaceWithDict(me.commands, variableDictionary)

    me.description = getDictArray ("__description")
    me.commandDescription = getDictArray ("__cmddescription")
    me.constraints = getDictArray("__constraints")
    #me.approve = None

    return me


  def isExecutable(self):
    return len(self.commands) > 0