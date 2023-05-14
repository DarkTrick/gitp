import argparse
import subprocess
from ...core.command import Command


class BranchCreate(Command):
    def __init__(self, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser('create',
                                            help='Create a new branch and switch to it')
        self._parser.set_defaults(func=self.run)
        self._parser.add_argument('branch_name',
                                  type=str,
                                  help='name for the new branch',
                                )

    def run(self, args: argparse.Namespace):
        commandArray = ["git", "checkout", "-b", args.branch_name]
        subprocess.run(commandArray)
