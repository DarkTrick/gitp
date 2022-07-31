
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