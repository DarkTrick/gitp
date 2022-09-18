from typing import List

from gitp.commands_config import commandDB
from command_parser.command_assembler import assembleCommand
from gitp.command_parser.dict_tree_finder.dict_tree_finder import dictTree_find

import subprocess

class Gitp:

  def __init__(self):
    pass


  def showHelp(self):
    help = """
  gitp [options] [commands]

    [options]
    =========
        --help
          Shows a description of the command

        --show
          Shows which git commands the command would trigger

        --explain
          Shows an explanation of what the git commands do



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

        branch delete local <remote branch name>
          Deletes local branch (DANGEROUS)


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

  def run(self, programName: str, parameters: List):


    # TODO: CLEAN UP!!!!!!
    # rewrite this whole parameter thing.
    # First off, this is not autotestable!
    if(len(parameters) == 0):
      self.showHelp()
      return
    if(len(parameters) == 1):
      if(parameters[0] == "--help"):
        self.showHelp()
        return

    # TODO: implement properly!
    showCommandHelp = False
    if(parameters[0] == "--help"):
      showCommandHelp = True
      parameters = parameters[1:]

    # TODO: implement properly!
    showCommandToRun = False
    if(parameters[0] == "--show"):
      showCommandToRun = True
      parameters = parameters[1:]

    # TODO: implement properly!
    explainCommand = False
    if(parameters[0] == "--explain"):
      explainCommand = True
      parameters = parameters[1:]

    result = assembleCommand(commandDB, parameters)

    if(result.failed()):
      print("Error: ", result.error)
      return

    if(showCommandHelp):
      print("\n".join(result.value.description))
      return

    if(showCommandToRun):
      print("The following commands will be run:")
      print("   ", end="")
      print("\n   ".join(result.value.commands))
      return

    if(explainCommand):

      print("The following commands will be run:")
      print("   ", end="")
      print("\n   ".join(result.value.commands))

      print("")
      print("Explanation:")
      print("   ", end="")
      print("\n   ".join(result.value.commandDescription))
      return


    # run command
    for strCommand in result.value.commands:
      commandArray: List[str] = strCommand.split(" ")
      subprocess.run(commandArray)
