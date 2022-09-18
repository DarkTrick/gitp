from typing import List, Dict

class Node:
  """
  Provides helper functions for
  """
  @staticmethod
  def isVariable(nodeKey: str):
    return nodeKey[:2] == "${" and nodeKey[-1] == "}"