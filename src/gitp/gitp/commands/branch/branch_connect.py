import argparse
import subprocess
from ...core.command import Command


class BranchConnect(Command):
    def __init__(self, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser('connect',
                                            help='Connect current branch with remote branch with the same name')
        self._parser.set_defaults(func=self.run)
        self._parser.add_argument('branch_name',
                                  type=str,
                                  help='name of the branch that should be connected',
                                )

    def run(self, args: argparse.Namespace):
        commandArray = ["git", "branch", "--set-upstream-to=origin/" + args.branch_name]
        subprocess.run(commandArray)
