import argparse
import subprocess

from ...core.gitutils.gitutils import git_getCurrentBranch

from ...core.cli_execute import cli_execute

from ...core.command_exception import CommandException
from ...core.command import Command


class BranchReset(Command):
    def __init__(self, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser('reset',
                                            help='Reset local changes to the remote state (Ignore untracked files, Ignore gitignore files)')
        self._parser.set_defaults(func=self.run)


    def run(self, args: argparse.Namespace):
        currentBranchResult = git_getCurrentBranch()

        currentBranch = currentBranchResult.getData()
        if(currentBranch == None):
            raise CommandException(currentBranchResult.getError())


        commandArray = ["git", "fetch","origin"]
        cli_execute(commandArray, raiseOnFailure=True)

        commandArray = ["git", "checkout", currentBranch]
        cli_execute(commandArray, raiseOnFailure=True)

        commandArray = ["git", "reset", "--hard","origin/" + currentBranch]
        cli_execute(commandArray, raiseOnFailure=True)

