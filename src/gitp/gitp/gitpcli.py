

import argparse
import subprocess
import sys
from typing import List

from .core.gitutils.gitutils import git_isInstalled

from .core.command_exception.command_exception import CommandException
from .commands.branch.branch import Branch
from .commands.branches.branches import Branches
from .commands.commit.commit import Commit

class GitpCli:
    def __init__(self):
        self._parser = argparse.ArgumentParser(prog='gitp', description='Tool for simplified git usage')
        self.subparsers = self._parser.add_subparsers(title='Actions',
                                                      required=True)

        # register subcommands
        Branch("branch", "b", self.subparsers)
        Branches("branches", "bs", self.subparsers)
        Commit("commit", "c", self.subparsers)


    def run(self):
      try:
        self.raiseIfGitNotAvailable(sys.argv)
        args = self._parser.parse_args()
        args.func(args)

      except CommandException as e:
        print(str(e))

      except Exception as e:
        raise e

    def raiseIfGitNotAvailable(self, args: List[str]):
      def letUserKnow(args: List[str]):
        if("-h" in args or "--help" in args):
          print("WARNING: Cannot find git. Please install git.")
          print("")
          return

        raise CommandException("FATAL ERROR: Cannot find git. Please install git.")


      if(not git_isInstalled()):
        letUserKnow(args)

      return True



