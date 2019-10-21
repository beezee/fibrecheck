from typing import Callable, TypeVar

A = TypeVar('A')
B = TypeVar('B')

def fibrecheck(ab: Callable[[A], B], ba: Callable[[B], A], a: A) -> None:
  res = ab(a)
  assert ab(ba(res)) == res
