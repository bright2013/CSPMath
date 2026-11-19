# Multiplication Principle 【2】

乘法原理

## Description

**Multiplication principle (rule of product)**: if a task is completed in **steps**,
and step 1 can be done in n₁ ways, step 2 in n₂ ways, …, step k in nₖ ways, then the
total number of ways is:

> n₁ · n₂ · … · nₖ

The principle applies when every combination of choices across the steps gives a
distinct valid outcome — the number of choices at each step may depend on earlier
steps, but must be *countable* at that point.

Typical phrasing: "first … then …", "choose one of each". A useful mental picture is
a tree: the number of leaves is the product of the branching factors along each path.

Addition vs. multiplication: **addition** splits one task into alternative cases
(either/or); **multiplication** chains sub-tasks that all must happen (and then).
Many problems need both — split into cases with addition, count each case with
multiplication.

## Examples

**Example 1.** 3 shirts and 4 pairs of trousers → 3 × 4 = 12 outfits.

**Example 2.** How many three-digit numbers are there? Hundreds digit: 9 choices
(1–9); tens and units: 10 each → 9 × 10 × 10 = 900.

**Example 3.** How many three-digit numbers have **distinct** digits?
Hundreds: 9; tens: 9 (0 allowed, but not the hundreds digit); units: 8 →
9 × 9 × 8 = 648.

**Example 4.** Number of binary strings of length 8: 2⁸ = 256. Number of license
plates with 2 letters followed by 3 digits: 26² × 10³ = 676 000.

**Example 5 (both principles).** How many even three-digit numbers with distinct
digits? Split by units digit (addition):
- units = 0: hundreds 9, tens 8 → 72;
- units ∈ {2,4,6,8}: 4 choices, hundreds 8 (not 0, not the units digit), tens 8 →
  4 × 8 × 8 = 256.
Total: 72 + 256 = 328.

**Example 6 (C++).** Verify by enumeration:

```cpp
int cnt = 0;
for (int h = 1; h <= 9; h++)
    for (int t = 0; t <= 9; t++)
        for (int u = 0; u <= 9; u++)
            if (u % 2 == 0 && h != t && t != u && h != u) cnt++;
// cnt == 328
```

## Practice

1. An ice-cream shop offers 5 flavors, 3 sizes and 2 cone types. How many different
   orders? *(Answer: 30.)*
2. How many four-digit numbers are there? How many are odd?
   *(Answer: 9·10³ = 9000; 9·10·10·5 = 4500.)*
3. In how many ways can 5 different books be arranged in a row on a shelf?
   *(Answer: 5! = 120.)*
4. How many strings of length 5 can be built from letters A–Z if no letter repeats?
   *(Answer: 26·25·24·23·22 = 7 893 600.)*
5. A password is 4 digits. How many passwords are there? How many have distinct
   digits? How many start with 0 and have distinct digits?
   *(Answer: 10⁴ = 10 000; 10·9·8·7 = 5040; 1·9·8·7 = 504.)*
6. Write a program that reads n and k and prints the number of length-k strings over
   an n-letter alphabet with no repeated letters (assume k ≤ n ≤ 26).
7. (Challenge) How many three-digit numbers are divisible by 5 and have distinct
   digits? *(Hint: split on units digit 0 vs 5. Answer: 9·8 + 8·8 = 136.)*
