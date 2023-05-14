import argparse


class Command:
  """
    Base class for commands.

    Background: Make sure commands have a unified interface
  """

  def __init__(self, parserMgr: argparse._SubParsersAction):
    pass

  def run(self, args: argparse.Namespace):
    pass