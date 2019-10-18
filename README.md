# Fibrecheck

Currently this is just notes. Code to follow shortly.


### Idea

Every function `f` gives rise to an equivalence class via its fibration `f-1`.

This new set has an idempotent split by the codomain of `f`, by taking `x . f-1 . f`, where `x` takes a preferred element (arbitrary works as well, but these are functions after all) for each set in `f-1 . f`

This means that `f . x . f-1` is `1(codom(f))`

Given a function under test, an arbitrary input, and a function from output to input (`x . f-1`), the inverse relationship between these two provided functions can be verified up to equivalence.

Given a means of accumulating generated inputs and outputs of the provided `x . f-1` across evaluations of a given property, the equivalence relation can be verified disjoint on completion.

The short version of this is, given a function to test, and a function that describes how to construct, for any given output, _one_ input that will produce the given output, _all_ inputs that should produce the given output can be verified.


### Composition

While tests of this nature might offer a reasonable answer (in terms of lost leverage) to the lack of a sophisticated type system capable of lowering cardinality of input and output sets in a meaningful way so as to promote run-time edge cases to type-checking, it does so only at a fairly low level (unit tests.)

In an environment with a sufficient type system, rules of composition can be captured and enforced by the type system, even up to tracking of side effects with varying degrees of precision. The typically anemic response to this in a less luxurious programming environment falls under a vaguely defined bucket of "integration tests."

As a corollary to the leverage gained by verification that `f . x . f-1 . f = f` at the level of an atomic unit of composition, given a function `g` such that `g . f`, and `g . y . g-1 = 1(codom(g))`, then `g . f . x . f-1 . y . g-1 . g . f = g . (f . x . f-1) . y . g-1 . g . f = g . 1(codom(f)) . y . g-1 . g . f = g . y . g-1 . g . f = (g . y . g-1) . g . f = 1(codom(g)) . g . f = g . f`

This means that a pair `(x-1, r)` for some function `x` where `x . r . x-1 = 1(codom(x))` forms an endofunctor `repr-input` in set, where `repr-input(id) = (id, {({a}, a)})`, and as shown in the previous paragraph `repr-input(g . f) = repr-input(g) . repr-input(f)`

What this means for "integration tests" is that you gain two new dimensions via verification of composed idempotents. Specifically, in "standard" anemic style testing, a known input `i` is fed to a composite process `f`, and assertions are made against the output, reflecting the specifications for the process under test. You have a single comparison, `(f(i) x expected output)`, alignment is a successful test, and disagreement means the behavior of the composite process is not consistent with the expected behavior.

With the availability of composite idempotents, for a composite process `f` implemented in terms of `g` and `h`, there are three comparisons possible, `(f(i) x f(repr-input(h . g)) x f(repr-input(f)))`. Disagreement between the first and third carries the same meaning as in the case of a known input against expected output outlined in the previous paragraph. Disagreement between the first and the second means the behavior of the composite process is not consistent with the composition of expectations for the process' constituent parts, and disagreement between the second and third means the composition of expectations for the process' consituent parts is not consistent with the expectations for the composite process. Utility of these added dimensions remains to be seen in practice, but generally (and arguably particularly in the area of verification) having more information is better than less.
