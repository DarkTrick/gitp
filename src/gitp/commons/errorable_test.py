import unittest

from commons.errorable import Errorable

class CommandCreatorTest(unittest.TestCase):

  def test_initialized_object_defaultValues(self):
    # setup

    # run
    subject = Errorable()

    # check
    self.assertEqual(subject.value, None, "value")
    self.assertEqual(subject.error, None, "error")



  def test_initialized_object_is_succeeded(self):
    # setup

    # run
    subject = Errorable()

    # check
    self.assertTrue(subject.succeeded(), "succeeded")
    self.assertFalse(subject.failed(), "failed")



  def test_failed_if_error(self):
    # setup
    subject = Errorable()

    # run
    subject.error = "a"

    # check
    self.assertTrue(subject.failed(), "failed")
    self.assertFalse(subject.succeeded(), "succeeded")


  def test_initialize_hasValue(self):
    # setup

    # run
    subject = Errorable()

    # check
    self.assertFalse(subject.hasValue())

  def test_hasValue(self):
    # setup
    subject = Errorable()

    # run
    subject.value = "a"

    # check
    self.assertTrue(subject.hasValue())
