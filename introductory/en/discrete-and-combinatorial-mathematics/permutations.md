# Permutations 【4】

排列

## Description

A **permutation** is an **ordered** arrangement. The number of ways to arrange m
elements chosen from n distinct elements in a row is:

> A(n, m) = n·(n−1)·…·(n−m+1) = n! / (n−m)!

Special case — the **full permutation** of n distinct elements: A(n, n) = n!.

Recall n! = 1·2·…·n with 0! = 1. Order matters: (a, b) and (b, a) are different
permutations. Compare with combinations, where order does not matter.

**Why the formula**: position 1 has n choices, position 2 has n−1 remaining, …,
position m has n−m+1 — then apply the multiplication principle.

**Permutations with repetition (bonus insight)**: if some elements are identical,
divide by the factorials of the multiplicities, e.g. arranging the letters of BALL:
4! / 2! = 12.

**In programming**, `std::next_permutation` enumerates all n! orderings of a
sequence — the standard brute-force tool for small n (n ≤ 8–10).

## Examples

**Example 1.** A(5, 3) = 5·4·3 = 60: ways to award gold/silver/bronze among
5 athletes.

**Example 2.** A(4, 4) = 4! = 24 ways to line up 4 people for a photo.

**Example 3.** In how many ways can 6 people sit in a row if two specific people A
and B must be adjacent? Glue A, B into one block: 5! arrangements of the block with
the rest, times 2 orders inside the block → 240.

**Example 4 (C++).** Enumerate all permutations of {1, 2, 3}:

```cpp
#include <algorithm>
int a[] = {1, 2, 3};
do {
    // 1 2 3, 1 3 2, 2 1 3, 2 3 1, 3 1 2, 3 2 1
} while (next_permutation(a, a + 3));
```

Note: `next_permutation` starts from sorted order; sort first if needed.

**Example 5 (C++).** Compute A(n, m) without big factorials:

```cpp
long long perm(long long n, long long m) {
    long long r = 1;
    for (long long i = 0; i < m; i++) r *= (n - i);
    return r;   // n·(n−1)·…·(n−m+1)
}
```

## Practice

1. Compute: A(6, 2), A(7, 3), 6!. *(Answer: 30; 210; 720.)*
2. How many 3-digit numbers can be formed from digits 1–6 with no repetition?
   *(Answer: A(6, 3) = 120.)*
3. 5 runners finish a race; no ties. How many possible rankings? *(Answer: 120.)*
4. In how many ways can the letters of the word MATH be arranged? Of the word BOOK?
   *(Answer: 4! = 24; 4!/2! = 12.)*
5. 8 people stand in a row; one specific person must be at an end. How many
   arrangements? *(Answer: 2 × 7! = 10 080.)*
6. How many permutations of {1,…,6} have 1 somewhere to the left of 2?
   *(Hint: exactly half of all permutations. Answer: 360.)*
7. Write a program using `next_permutation` that reads n (n ≤ 8) and a target
   permutation, and prints its 1-based position in lexicographic order.
8. (Challenge) Derangements: in how many ways can 4 letters be put into 4 addressed
   envelopes so that no letter is in the correct envelope? *(Answer: 9.)*
