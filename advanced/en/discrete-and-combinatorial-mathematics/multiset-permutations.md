# Permutations of Multisets 【6】

多重集上的排列

## Description

**Problem**: arrange the n objects of a multiset in a row, where objects of the same
type are indistinguishable. If type i has multiplicity nᵢ and n = n₁ + … + nₖ, the
number of distinct arrangements is the **multinomial coefficient**:

> n! / (n₁! · n₂! · … · nₖ!)

**Why**: start from n! arrangements of distinct objects; permuting the nᵢ identical
copies of type i among themselves (nᵢ! ways) does not change the arrangement, so
divide by each nᵢ!.

Equivalent view: choose positions for type 1 (C(n, n₁)), then for type 2
(C(n−n₁, n₂)), … — the product telescopes to the same formula.

## Examples

**Example 1.** Arrangements of BALL: 4!/2! = 12.

**Example 2.** Arrangements of MISSISSIPPI: 11!/(1!·4!·4!·2!) = 39916800/1152 =
34 650.

**Example 3.** How many distinct paths from (0,0) to (4,3) using unit steps right/up?
Each path is an arrangement of {R×4, U×3}: 7!/(4!·3!) = 35 = C(7, 3).

**Example 4.** In how many ways can 10 identical candies be… — careful: identical
objects into a *row* is the multiset permutation only when the types are positions.
For distributing identical candies to distinct children, see
[combinations of multisets](multiset-combinations.md).

**Example 5 (C++).** Compute 11!/(4!·4!·2!) safely — cancel as you go or use
multiplicative combination steps:

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
   *(Answer: 5!/2!… L×2, E×2 → 5!/(2!2!) = 30; 6!/(3!·2!) = 60;
   11!/(5!·2!·2!) = 83 160.)*
2. How many distinct 10-bit strings contain exactly six 1s? *(Answer: C(10, 6) =
   210.)*
3. A bookshelf holds 4 identical math books, 3 identical novels and 2 identical
   comics. How many distinct arrangements? *(Answer: 9!/(4!·3!·2!) = 1260.)*
4. How many paths from (0,0) to (6,6)? From (0,0) to (6,6) passing through (2,2)?
   *(Answer: C(12,6) = 924; C(4,2)·C(8,4) = 6·70 = 420.)*
5. In how many ways can the letters of SUCCESS be arranged so that the two C's are
   not adjacent? *(Hint: total minus adjacent; total = 7!/(3!·2!) = 420; treat CC as
   one block: 6!/3! = 120. Answer: 300.)*
6. Write a program that reads a string (length ≤ 20) and prints the number of its
   distinct permutations — watch for overflow beyond n = 20.
7. (Challenge) Arrangements of {a×2, b×2, c×2} with no two identical letters
   adjacent: use inclusion–exclusion. *(Answer: 30.)*
