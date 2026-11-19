# Permutations of Multisets 【6】

多重集上的排列

## Description

**Problem**: arrange the n objects of a multiset in a row, where objects of the
same type are indistinguishable. If type i has multiplicity nᵢ and
n = n₁ + … + nₖ, the number of distinct arrangements is the **multinomial
coefficient**:

> n! / (n₁! · n₂! · … · nₖ!)

**Why it works — two proofs, two habits of mind:**

* *Division argument*: start from n! arrangements of distinct objects. Permuting
  the nᵢ identical copies of type i among themselves (nᵢ! ways) never changes
  the visible arrangement, and every equivalence class has exactly
  n₁!·n₂!·…·nₖ! members — so divide. "Count the labeled version, then divide by
  the symmetry" is one of the most reusable tricks in combinatorics.
* *Sequential placement*: choose positions for type 1 (C(n, n₁) ways), then for
  type 2 among the rest (C(n−n₁, n₂)), and so on. The product telescopes to the
  same formula — verify the cancellation once and you own the formula forever.

**Lattice-path view**: a path from (0,0) to (p, q) with unit right/up steps is
an arrangement of {R×p, U×q} — hence C(p+q, p) paths. Many grid problems are
multiset permutations in disguise, and adding a restriction (e.g. "never cross
the diagonal") leads straight to [Catalan numbers](catalan.md).

**Pitfall**: this formula is for arranging a *fixed* multiset. "How many
multisets can be formed…" or "distribute identical objects into boxes" are
*different* problems — see [combinations of multisets](multiset-combinations.md).

## Examples

**Example 1.** Arrangements of BALL: 4!/2! = 12.

**Example 2.** Arrangements of MISSISSIPPI: 11!/(1!·4!·4!·2!) = 39916800/1152 =
34 650.

**Example 3.** How many distinct paths from (0,0) to (4,3) using unit steps
right/up? Each path is an arrangement of {R×4, U×3}: 7!/(4!·3!) = 35 = C(7, 3).

**Example 4.** In how many ways can 10 identical candies be… — careful:
identical objects into a *row* is a multiset permutation only when the types are
positions. For distributing identical candies to distinct children, see
[combinations of multisets](multiset-combinations.md).

**Example 5.** Non-adjacency by subtraction: arrangements of {A×3, B×2} with
the two B's *not* adjacent = total − (B's adjacent) = 5!/(3!·2!) − 4!/3! =
10 − 4 = 6. (Treat adjacent B's as one block "BB".)

**Example 6 (C++).** Compute 11!/(4!·4!·2!) safely — never compute 11! first if
you can cancel as you go; a chain of combinations keeps intermediates small:

```cpp
long long r = 1;
int n = 11;
// choose positions of the I's, then S's, then P's
auto C = [](int n, int m) {
    long long r = 1;
    for (int i = 1; i <= m; i++) r = r * (n - m + i) / i;
    return r;
};
r = C(11, 4) * C(7, 4) * C(3, 2);   // 330 * 35 * 3 = 34650
```

## Practice

1. Count distinct arrangements of: LEVEL; BANANA; ABRACADABRA.
   *(Answer: 5!/(2!·2!) = 30; 6!/(3!·2!) = 60; 11!/(5!·2!·2!) = 83 160.)*
2. How many distinct 10-bit strings contain exactly six 1s? *(Answer: C(10, 6) =
   210.)*
3. A bookshelf holds 4 identical math books, 3 identical novels and 2 identical
   comics. How many distinct arrangements? *(Answer: 9!/(4!·3!·2!) = 1260.)*
4. How many paths from (0,0) to (6,6)? From (0,0) to (6,6) passing through
   (2,2)? *(Answer: C(12,6) = 924; C(4,2)·C(8,4) = 6·70 = 420.)*
5. In how many ways can the letters of SUCCESS be arranged so that the two C's
   are not adjacent? *(Hint: total minus adjacent; total = 7!/(3!·2!) = 420;
   treat CC as one block: 6!/3! = 120. Answer: 300.)*
6. Write a program that reads a string (length ≤ 20) and prints the number of
   its distinct permutations — watch for overflow beyond n = 20.
7. How many arrangements of {a×2, b×2, c×1} have c between the two a's (not
   necessarily adjacent)? *(Hint: among the 5!/(2!·2!) = 30 arrangements, the
   relative order of a, c, a′ is uniform over 3!/2! = 3 patterns… Answer: 10.)*
8. (Challenge) Arrangements of {a×2, b×2, c×2} with no two identical letters
   adjacent: use inclusion–exclusion. *(Answer: 30.)*
