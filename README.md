# Fibrecheck

Currently this is just notes. Code to follow shortly.


### Idea

Every function `f` gives rise to an equivalence class via its fibration `f-1`.

This new set has an idempotent split by the codomain of `f`, by taking `f-1 . f . x`, where `x` takes a preferred element (arbitrary works as well, but these are functions after all) for each set in `f-1 . f`

This means that `f . x . f-1` is `1(codom(f))`

Given a function under test, an arbitrary input, and a function from output to input (`x . f-1`), the inverse relationship between these two provided functions can be verified up to equivalence.

Given a means of accumulating generated inputs and outputs of the provided `x . f-1` across evaluations of a given property, the equivalence relation can be verified disjoint on completion.

The short version of this is, given a function to test, and a function that describes how to construct, for any given output, _one_ input that will produce the given output, _all_ inputs that should produce the given output can be verified.
