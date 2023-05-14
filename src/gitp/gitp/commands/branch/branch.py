import argparse
from .branch_create import BranchCreate
from .branch_push import BranchPush
from .branch_connect import BranchConnect
from .branch_rename import BranchRename
from .branch_reset import BranchReset
from .branch_delete import BranchDelete


class Branch:
    def __init__(self, command: str, command_short: str, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser(
                        command,
                        aliases=[command_short],
                         help='branch help')
        self.subparsers = self._parser.add_subparsers(
                                                      description='Branch actions',
                                                      dest='command',
                                                      required=True)

        # register subcommands
        BranchCreate(self.subparsers)
        BranchPush(self.subparsers)
        BranchConnect(self.subparsers)
        BranchRename(self.subparsers)
        BranchReset(self.subparsers)
        BranchDelete("delete", "del", self.subparsers)