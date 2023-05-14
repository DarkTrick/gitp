
import subprocess

from ...core.types.errorable.errorable import Errorable


def git_getCurrentBranch() -> Errorable[str]:
  """
    Return current branch or raise on error
  """

  commandArray = ["git","branch","--show-current"]
  result = subprocess.run(commandArray, capture_output=True, text=True)
  currentBranch = result.stdout.split("\n")[0]

  if(currentBranch == "" or currentBranch == None):
    return Errorable[str](error="Error: No branch found to reset to (found: " + str(result.stdout) + ")")

  return Errorable[str](data=currentBranch)


def git_isInstalled() -> bool:
  try:
    commandArray = ["git", "--version"]
    result = subprocess.run(commandArray, capture_output=True, text=True)

    if (result.stderr != ""):
      return False

    # git is available
    return True

  except Exception as e:
    pass

  return False

def git_connectBranchToRemote(branch: str):
  commandArray = ["git","push","--set-upstream","origin",branch]
  result = subprocess.run(commandArray, capture_output=True, text=True)

  return result