import argparse
import subprocess
from ...core.command import Command
from ._argument_type_commit import argument_type_commit


class CommitDelete(Command):
    def __init__(self, parserMgr: argparse._SubParsersAction):
        self._parser = parserMgr.add_parser('delete',
                                            help='Delete commits (do not keep the changes)')
        self._parser.set_defaults(func=self.run)
        self._parser.add_argument('commit',
                                  type=argument_type_commit,
                                  help='`last` = delete last commit.\n`<number>` = delete the last x commits. \n`<commitId>` = delete every commit between now and the given commit ID.',
                                )

        # TODO: this works/runs fine, but the help is very difficult to understand.
        # It should look like this:
        #
        # last          delete last commit
        # number        delete the last x commits
        # commitId      delete every commit between now and the given commit ID

    def run(self, args: argparse.Namespace):
        numberOfCommits = args.history
        commandArray = ["git", "reset", "--hard", numberOfCommits]
        #print (commandArray)
        subprocess.run(commandArray)
