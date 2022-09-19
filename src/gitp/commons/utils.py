
from ast import Dict
import typing


def dict_get(dict, key, default = None):
  """
    returns dict[key], of `default`, if key not existend
  """
  if (not key in dict):
    return default

  return dict[key]


def isArray(value) -> bool:
  """does not work for numpy arrays"""
  return isinstance(value, typing.List)


def makeArray(value) -> typing.List:
  """returns an array. If `value` is an array, return `value)"""
  if (None == value):
    return []

  if(isArray(value)):
    return value

  return [value]

def strArray_toString(strArray: list[str], prefix: str = "") -> str:
  """Converts a list of strings to a string (one line per item).
     `prefix` is prefexed on every line
  """
  return (prefix + "\n").join(strArray)

def string_replaceWithDict(value: str, replaceDict: Dict):
  """
  Replaces substrings in `value` with values defined in `variableDict`
  """
  ret = value
  for oldStr, newStr in replaceDict.items():
    ret = ret.replace(oldStr, newStr)

  return ret


def stringArray_replaceWithDict(values: typing.List[str], variableDict: Dict) -> typing.List[str]:
  """
  like string_replaceWithDict, but works on a string array
  """
  ret = []
  for value in values:
    newValue = string_replaceWithDict(value, variableDict)
    ret.append(newValue)

  return ret