import argparse
from .branches_show import BranchesShow
from ...core.command import Command


class Branches(Command):
    def __init__(self, command: str, command_short: str, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser(
                        command,
                        aliases=[command_short],
                        help='Actions on branches')
        self._parser.set_defaults(func=self.run)
        self.subparsers = self._parser.add_subparsers(
                                                      description='Actions on branches',
                                                      dest='action',
                                                      required=False)

        # register subcommands
        BranchesShow(self.subparsers)

    def run(self, args: argparse.Namespace):
      BranchesShow.run(None)