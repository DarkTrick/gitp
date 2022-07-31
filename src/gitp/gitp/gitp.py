from typing import List

from gitp.commands_config import commandDB
from command_parser.command_assembler import assembleCommand
from command_parser.dict_tree_finder import dictTree_find

import subprocess

class Gitp:

  def __init__(self):
    pass

  def run(self, programName: str, parameters: List):


    # TODO: CLEAN UP!!!!!!
    # rewrite this whole parameter thing.
    # First off, this is not autotestable!
    if(len(parameters) > 0 and parameters[0] == "--help"):
      parameters = parameters[1:]
      res = dictTree_find(commandDB, parameters)
      if(res.branch == None):
        print("Error: command unknown")
        return

      expl = ""
      if(len(parameters) == 0):
        expl = programName
      else:
        expl = "`" + " ".join (parameters) + "`"

      print(expl + " has the following subcommands:")

      for branchKey, branch in res.branch.items():
        print("   " + str(branchKey))
      return

    result = assembleCommand(commandDB, parameters)

    if(result.failed()):
      print("Error: ", result.error)
      return


    for strCommand in result.value.commands:
      commandArray: List[str] = strCommand.split(" ")
      subprocess.run(commandArray)
