

from typing import Any, Generic


class Errorable:
  def __init__(self, value=None, error=None):
    self.value: Any = None
    self.error: str | None = None

  def succeeded(self):
    return (self.error == "" or self.error == None)


  def failed(self):
    return not self.succeeded()

  def hasValue(self):
    return self.value != None