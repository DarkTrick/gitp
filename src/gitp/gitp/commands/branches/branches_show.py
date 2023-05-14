import argparse
import subprocess
from typing import Union
from ...core.command import Command


class BranchesShow(Command):
    def __init__(self, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser('show',
                                            help='show available branches')
        self._parser.set_defaults(func=BranchesShow.run)

        self._parser.add_argument("--local",
                                  action="store_true",
                                  help="Show local branches.")
        self._parser.add_argument("--remote",
                                  action="store_true",
                                  help="Show remote branches.")
        self._parser.add_argument("--all",
                                  action="store_true",
                                  help="Show local and remote branches (default: true).")

    @staticmethod
    def run(args: Union[argparse.Namespace, None]):
      displayRange = "-a"
      if(args):
        if(args.remote):  displayRange = "-r"
        if(args.local):  displayRange = "-l"
        if(args.all):  displayRange = "-a"


      commandArray = ["git", "branch", displayRange]
      subprocess.run(commandArray)
