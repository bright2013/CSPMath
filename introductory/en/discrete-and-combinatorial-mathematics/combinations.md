# Combinations 【4】

组合

## Description

A **combination** is an **unordered** selection. The number of ways to choose m
elements from n distinct elements, where the order of selection does not matter, is
the binomial coefficient:

> C(n, m) = n! / (m! · (n−m)!) = A(n, m) / m!

Dividing A(n, m) by m! removes the m! different orderings of the same selection:
{1, 2, 3} and {3, 1, 2} are the same combination but different permutations.

**Key properties:**

* Symmetry: C(n, m) = C(n, n−m) — choosing what to take = choosing what to leave.
* Recurrence (Pascal's rule): C(n, m) = C(n−1, m−1) + C(n−1, m).
* Row sum: C(n, 0) + C(n, 1) + … + C(n, n) = 2ⁿ (all subsets of an n-set).
* Boundary: C(n, 0) = C(n, n) = 1.

**Computing C(n, m) safely**: cancel before multiplying, or use the recurrence
(dynamic programming). Values grow fast — C(60, 30) ≈ 1.18 × 10¹⁷ still fits in
`long long`, C(67, 33) does not.

## Examples

**Example 1.** C(5, 2) = 10: ways to pick 2 of 5 players for a doubles pair.
Check: A(5, 2) / 2! = 20 / 2 = 10.

**Example 2.** C(10, 3) = 10! / (3!·7!) = (10·9·8)/(3·2·1) = 120.

**Example 3.** A committee of 3 from 7 boys and 4 girls, with exactly 2 girls:
choose the girls C(4, 2) = 6, choose the boy C(7, 1) = 7 → 6 × 7 = 42
(multiplication principle across the two groups).

**Example 4.** How many subsets does an 8-element set have? 2⁸ = 256 — the row sum
of binomial coefficients.

**Example 5 (C++).** C(n, m) by multiplicative formula:

```cpp
long long comb(int n, int m) {
    if (m > n - m) m = n - m;      // symmetry
    long long r = 1;
    for (int i = 1; i <= m; i++)
        r = r * (n - m + i) / i;   // division is exact at each step
    return r;
}
```

**Example 6 (C++).** C(n, m) by Pascal's recurrence (needed when values must be
taken modulo a prime):

```cpp
for (int i = 0; i <= n; i++) {
    C[i][0] = C[i][i] = 1;
    for (int j = 1; j < i; j++)
        C[i][j] = C[i-1][j-1] + C[i-1][j];
}
```

## Practice

1. Compute: C(6, 3), C(8, 2), C(10, 4). *(Answer: 20; 28; 210.)*
2. From 12 students, in how many ways can a group of 4 be chosen? *(Answer: 495.)*
3. How many diagonals does a convex n-gon have?
   *(Hint: C(n, 2) counts all segments between vertices; subtract the n sides.
   Answer: n(n−3)/2.)*
4. A pizza shop has 8 toppings; you must choose exactly 3. How many combinations?
   *(Answer: 56.)*
5. From 5 men and 6 women, choose a committee of 5 with at least 3 women.
   *(Hint: split into cases of exactly 3, 4, 5 women and add.
   Answer: C(6,3)C(5,2) + C(6,4)C(5,1) + C(6,5) = 200 + 75 + 6 = 281.)*
6. Verify C(10, 3) = C(10, 7) and C(8, 0) + … + C(8, 8) = 2⁸ by direct computation.
7. Write a program that reads n, m and prints C(n, m) — handle n up to 60 without
   overflow, and say what breaks at larger n.
8. (Challenge) How many paths go from (0, 0) to (7, 5) moving only right (R) or
   up (U)? *(Hint: every path is a sequence of 12 moves, choose which 5 are U.
   Answer: C(12, 5) = 792.)*
