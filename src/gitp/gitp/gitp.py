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
    if(len(parameters) == 0 or parameters[0] == "--help"):
      help = """
gitp [commands]

  branch
  ======

      branch checkout remote <remote branch name>
        Checkout and switch to <remote branch name>

      branch create <branch name>
        Create a new branch and switch to it

      branch connect to <remote branch name>
        Connect current branch with remote branch with the same name

      branch rename <new branch name>
        Renames the current branch to <new branch name>

      branch reset to remote <remote branch name>
        Reset local changes to the remote state
        Ignore untracked files
        Ignore gitignore files

      branch delete remote <remote branch name>
        Deletes remote branch (DANGEROUS)

  branches
  ========

      branches show remote

      branches show local

      branches show all

  commit
  ======

      commit delete last
        Delete last commit and discard all changes

      commit undo last
        Undo last commit but keep the changes


      """
      print(help)
      return


    result = assembleCommand(commandDB, parameters)

    if(result.failed()):
      print("Error: ", result.error)
      return


    for strCommand in result.value.commands:
      commandArray: List[str] = strCommand.split(" ")
      subprocess.run(commandArray)
