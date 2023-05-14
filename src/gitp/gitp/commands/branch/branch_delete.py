import argparse
import subprocess
from typing import Union
from ...core.command import Command
from ...core.command_exception import CommandException



class BranchDelete(Command):
    def __init__(self, command: str, command_short: str, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser(command,
                                            aliases=[command_short],
                                            help='Delete branch from `local` or `remote` or both. (If no option is given, remote and local will be deleted.)')
        self._parser.set_defaults(func=self.run)

        self._parser.add_argument("--local",
                                  action="store_true",
                                  help="Delete only local branch.")
        self._parser.add_argument("--remote",
                                  action="store_true",
                                  help="Delete only remote branch.")

        self._parser.add_argument('branch',
                                  help='branch to delete')

    def run(self, args: argparse.Namespace):
        local = args.local
        remote = args.remote

        if(local == False and remote == False):
          local = True
          remote = True

        branchToDelete = args.branch

        if (remote):
          handleImportantBranches(branchToDelete)

          commandArray = ["git", "push", "origin", "--delete", branchToDelete]
          #print(commandArray)
          subprocess.run(commandArray)

        if (local):
          commandArray = ["git", "branch", "-D", branchToDelete]
          #print(commandArray)
          subprocess.run(commandArray)


def handleImportantBranches(branchToDelete: str) -> str:
  """
    If target branch is important, get re-assurance from user
    and raise if necessary.
  """

  importantBranches = ["master", "main", "develop", "dev", "prod", "production", "release", "trunc"]

  if(branchToDelete in importantBranches):
    print("  DANGER ZONE")
    answer = input("  Are you sure to delete `${branchToDelete}` from remote? (yes/no) ")
    if(answer != "yes"):
      raise CommandException("Aborted.")

  return branchToDelete