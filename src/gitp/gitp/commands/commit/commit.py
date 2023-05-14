from .commit_undo import CommitUndo
from .commit_delete import CommitDelete

class Commit:
    def __init__(self, command: str, command_short: str, parent_parser):
      self._parser = parent_parser.add_parser(
                    command,
                    aliases=[command_short],
                    help='Do somethings with commits')
      self.subparsers = self._parser.add_subparsers(
                                                    description='Commit actions',
                                                    dest='command',
                                                    required=True)

      # register subcommands
      CommitDelete(self.subparsers)
      CommitUndo(self.subparsers)
