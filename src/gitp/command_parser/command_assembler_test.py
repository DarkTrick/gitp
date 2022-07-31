import unittest
from command_parser.command_assembler import assembleCommand

class CommandAssemblerTest(unittest.TestCase):


  def test_command_not_found(self):
    # setup
    cmdDB = {}
    input = ["asdf"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    self.assertTrue(actual.failed())



  def test_command_found(self):
    # setup
    cmdDB = {"existingCommand": {"__cmd": ["foo"]}}
    input = ["existingCommand"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    with self.subTest("Correct status?"):
      self.assertTrue(actual.succeeded())

    with self.subTest("Correct type?"):
      self.assertTrue(actual != None)

    with self.subTest("Correct content?"):
     self.assertEqual(len(actual.value.commands), 1)
     self.assertEqual(actual.value.commands[0], "foo")




  def test_path_with_no_command(self):
    # setup
    cmdDB = {"existingCommand": {"a": "a"}}
    input = ["existingCommand"]

    # run
    actual = assembleCommand(cmdDB,input)

    # check
    self.assertTrue(actual.failed())
