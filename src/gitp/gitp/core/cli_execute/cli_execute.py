
import subprocess
from ...core.command_exception import CommandException
from typing import List


def cli_execute(commandArray: List[str], raiseOnFailure=False):

  if(raiseOnFailure):
    result = subprocess.run(commandArray, capture_output=True, text=True)
    if result.returncode != 0:
      customError = "Error: Execution of git command failed (`" + " ".join(commandArray) + "`)"
      raise CommandException(customError + "\n" + result.stderr)

    if(result.stdout != ""):
      print(result.stdout)

  # just normal running
  subprocess.run(commandArray)
