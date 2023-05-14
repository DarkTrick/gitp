import argparse
import subprocess

from ...core.command_exception.command_exception import CommandException

from ...core.gitutils import gitutils
from ...core.command import Command


class BranchPush(Command):
    def __init__(self, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser('push',
                                            help='Push branch to remote')
        self._parser.set_defaults(func=self.run)

    def run(self, args: argparse.Namespace):
        commandArray = ["git", "push"]
        result = subprocess.run(commandArray, capture_output=True, text=True)

        if(result.returncode == 128):
          branchResult = gitutils.git_getCurrentBranch()
          branch = branchResult.getData()
          if(not branch):
            raise CommandException("Error retrieving current branch: " + str(branchResult.getError()))

          result = gitutils.git_connectBranchToRemote(branch)
          if(result.returncode == 0):
            result = subprocess.run(commandArray, capture_output=True, text=True)

        if(result.stderr):
          raise CommandException(result.stderr)

        if(result.stdout):
          print(result.stdout)

