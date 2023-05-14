
from typing import Any, Union

from typing import TypeVar, Generic
T = TypeVar('T')  # Define a type variable 'T'

class Errorable(Generic[T]):
  """
    Constraint: If `error` is "None", `data` is set
  """

  def __init__(self, data: Union[T, None] = None, error: Union[str, None] = None):
    self._error: Union[str, None] = error
    self._data: Union[T, None] = data
    self._checkConstraints()

  def _checkConstraints(self):
    if (self._error != None and self._data != None):
      raise Exception("Programming error: Errorable's error and data must not be set at the same time")

    if (self._error == None and self._data == None):
      raise Exception("Programming error: Errorable's error and data must not be None at the same time")

  def getError(self):
    return self._error

  def getData(self):
    return self._data