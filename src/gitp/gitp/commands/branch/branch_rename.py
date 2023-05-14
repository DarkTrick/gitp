import argparse
import subprocess
from ...core.command import Command


class BranchRename(Command):
    def __init__(self, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser('rename',
                                            help='Renames the current branch to `new_name`')
        self._parser.set_defaults(func=self.run)
        self._parser.add_argument('new_name',
                                  type=str,
                                  help='new name of the current branch',
                                )

    def run(self, args: argparse.Namespace):
        commandArray = ["git", "branch", "-m", args.new_name]
        subprocess.run(commandArray)
