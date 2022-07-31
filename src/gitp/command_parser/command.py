from typing import List, Dict
from commons.utils import makeArray, dict_get

class Command:

  def __init__(self):
    self.commands: List = []
    self.description: List = []
    self.commandDescription: List = []
    self.constraints: List = []
    self.approve = None


  @staticmethod
  def fromDict(dict: Dict):

    """
    Create `Command` from a string dictionary

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
    __constraints:
        Type: Array
        Set contraints for a command. E.g. branches the command will
        not work on
        Constraints:
          - `disabled for: $branchname`
            - Will not allow the command to run for the branch $branchname.

    __approve:
      Type: object
          Spawns a question asked the user prior to run the command.

          _msg:
            Type: Array
            Text shown on screen
          _actions
            Type: Array of key-value pairs:
            key: possible answer to type in
                Empty key = empty input / unknown input
            value: command to be executed.
                `_run` = run the command.
                `_abort` = abort the execution of the command immediately.

    """

    def getDictArray(key) -> List:
      return makeArray(dict_get(dict, key, []))

    me = Command()
    me.commands = getDictArray ("__cmd")
    me.description = getDictArray ("__description")
    me.commandDescription = getDictArray ("__cmddescription")
    me.constraints = getDictArray("__constraints")
    #me.approve = None

    return me


  def isExecutable(self):
    return len(self.commands) > 0