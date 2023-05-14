import argparse
import subprocess
from ...core.command import Command
from ._argument_type_commit import argument_type_commit


class CommitUndo(Command):
    def __init__(self, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser('undo',
                                            help='Undo commits (keep changes)')
        self._parser.set_defaults(func=self.run)
        self._parser.add_argument('commit',
                                  type=argument_type_commit,
                                  help='`last` = undo last commit.\n`<number>` = undo the last x commits. \n`<commitId>` = undo every commit between now and the given commit ID.',
                                )

        # TODO: this works/runs fine, but the help is very difficult to understand.
        # It should look like this:
        #
        # last          undo last commit
        # number        undo the last x commits
        # commitId      undo every commit between now and the given commit ID

    def run(self, args: argparse.Namespace):
        numberOfCommits = args.history
        commandArray = ["git", "reset", numberOfCommits]
        subprocess.run(commandArray)
