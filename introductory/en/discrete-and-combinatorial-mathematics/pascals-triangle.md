# Pascal's (Yang Hui) Triangle 【4】

杨辉三角

## Description

**Pascal's triangle** (known in China as **Yang Hui's triangle**, 杨辉三角, recorded
by Yang Hui in 1261) arranges the binomial coefficients in rows. Row n (starting
from row 0) is:

> C(n, 0), C(n, 1), …, C(n, n)

```
1
1   1
1   2   1
1   3   3   1
1   4   6   4   1
1   5  10  10   5   1
```

**Construction rule**: every entry equals the sum of the two entries above it:

> C(n, m) = C(n−1, m−1) + C(n−1, m)

This is exactly Pascal's rule for combinations, so the triangle *is* the table of
binomial coefficients.

**Properties worth knowing:**

* Symmetry: each row reads the same forwards and backwards (C(n, m) = C(n, n−m)).
* Row sum: row n sums to 2ⁿ.
* Binomial theorem: (a + b)ⁿ = Σₖ C(n, k) aⁿ⁻ᵏ bᵏ — e.g. (a+b)⁴ = a⁴ + 4a³b +
  6a²b² + 4ab³ + b⁴.
* The entries along the diagonals are the counting numbers, triangular numbers,
  tetrahedral numbers, …

**In programming** the triangle is computed by simple dynamic programming — the same
recurrence as for C(n, m), and the standard way to get all binomial coefficients up
to n in O(n²) time.

## Examples

**Example 1.** Row 5: 1, 5, 10, 10, 5, 1. Check 10 = 4 + 6 (the two entries above).

**Example 2.** Expand (a + b)³ using row 3: a³ + 3a²b + 3ab² + b³.

**Example 3.** Compute (1.01)⁴ approximately: (1 + 0.01)⁴ = 1 + 4(0.01) +
6(0.01)² + 4(0.01)³ + (0.01)⁴ ≈ 1.04060401.

**Example 4 (C++).** Print the first n rows:

```cpp
long long C[35][35];
for (int i = 0; i < n; i++) {
    for (int j = 0; j <= i; j++) {
        C[i][j] = (j == 0 || j == i) ? 1 : C[i-1][j-1] + C[i-1][j];
        cout << C[i][j] << " ";
    }
    cout << "\n";
}
```

**Example 5.** The sum of row 10 is 2¹⁰ = 1024 — count the subsets of a 10-element
set by size: C(10,0) + C(10,1) + … + C(10,10).

## Practice

1. Write out rows 6 and 7 of Pascal's triangle.
   *(Answer: 1 6 15 20 15 6 1; 1 7 21 35 35 21 7 1.)*
2. What is the sum of row 12? *(Answer: 4096.)*
3. Expand (a + b)⁵. *(Answer: a⁵ + 5a⁴b + 10a³b² + 10a²b³ + 5ab⁴ + b⁵.)*
4. Find the coefficient of x³ in (1 + x)⁸. *(Answer: C(8, 3) = 56.)*
5. Compute (2 + 1)⁵ and (2 − 1)⁵ via the binomial theorem; what do you get when you
   add the two expansions? *(Answer: 3⁵ = 243 and 1; adding cancels odd powers.)*
6. Write a program that prints the first n rows of Pascal's triangle (n ≤ 30) and
   checks that each row sums to a power of 2.
7. (Challenge) Hockey-stick identity: C(2,2) + C(3,2) + C(4,2) + … + C(8,2) =
   C(9, 3). Verify numerically and find it in the triangle. *(Answer: 84.)*
