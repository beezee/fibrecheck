from typing import Callable, TypeVar

A = TypeVar('A')
B = TypeVar('B')

# let `ab` be the function under test, and `a` be a generated input
# then `ba` is the fibration of `ab`, followed by some `x` which
# chooses a representative element for each fiber
# while you may never implement explicitly this way in practice,
# the mathematical construction is universal, so the composite
# `(x . ba)` is always defineable, and is highly likely to express
# a very thorough degree of specified properties for `ab`
def fibrecheck(ab: Callable[[A], B], ba: Callable[[B], A], a: A) -> None:
  res = ab(a)
  assert ab(ba(res)) == res
