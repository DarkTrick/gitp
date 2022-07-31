from typing import List

from gitp.commands_config import commandDB
from command_parser.command_assembler import assembleCommand

import subprocess

class Gitp:

  def __init__(self):
    pass

  def run(self, programName: str, paramters: List):
    result = assembleCommand(commandDB, paramters)

    if(result.failed()):
      print("Error: ", result.error)
      return

    for strCommand in result.value.commands:
      commandArray: List[str] = strCommand.split(" ")
      subprocess.run(commandArray)
