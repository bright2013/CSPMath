# Addition Principle 【2】

加法原理

## Description

**Addition principle (rule of sum)**: if a task can be completed in one of several
**mutually exclusive** cases, and case i can be done in nᵢ ways, then the total
number of ways is:

> n₁ + n₂ + … + nₖ

The crucial condition is that the cases **do not overlap** — every outcome belongs
to exactly one case. If cases overlap, adding counts duplicates, and you must fix it
with inclusion–exclusion: |A ∪ B| = |A| + |B| − |A ∩ B|.

Typical phrasing: "either … or …", "by train **or** by bus". Choosing the case split
(classification, 分类) is often the whole solution; a good split has no overlap and
no omission (不重不漏).

## Examples

**Example 1.** Travel from A to B by one of 3 trains or one of 4 buses:
3 + 4 = 7 ways.

**Example 2.** Count two-digit numbers whose digits sum to 9, split by tens digit:
18, 27, 36, 45, 54, 63, 72, 81, 90 → 9 numbers. (Each case — tens digit fixed to
d — contributes exactly one number.)

**Example 3.** How many integers in [1, 100] are divisible by 3 **or** by 5?
The cases "divisible by 3" (33) and "divisible by 5" (20) **overlap** in multiples
of 15 (6). Correct count: 33 + 20 − 6 = 47. Adding directly would be wrong.

**Example 4 (C++).** Count numbers in [1, n] ending in digit 0 or 5:

```cpp
long long ans = 0;
for (int i = 1; i <= n; i++)
    if (i % 10 == 0 || i % 10 == 5) ans++;   // two disjoint cases
```

**Example 5.** A menu has 4 appetizers, 6 mains and 3 desserts. If you order exactly
one dish, you have 4 + 6 + 3 = 13 choices.

## Practice

1. A bookshelf has 5 math books and 7 novels. In how many ways can you pick one
   book? *(Answer: 12.)*
2. How many integers in [1, 200] are divisible by 2 or by 3?
   *(Answer: 100 + 66 − 33 = 133.)*
3. How many three-digit numbers have all digits even? How many have all digits odd?
   How many have all digits of the same parity? *(Answer: 4·5·5 = 100; 5³ = 125;
   100 + 125 = 225.)*
4. From 4 red, 3 green and 5 blue balls, in how many ways can you draw one ball that
   is red or blue? *(Answer: 4 + 5 = 9.)*
5. Count the integers in [1, 1000] that contain the digit 7. *(Hint: count the
   complement — numbers with no digit 7 — then subtract from 1000. Answer: 271.)*
6. Write a program that reads n and counts the integers in [1, n] divisible by
   exactly one of 3 and 5 (not both).
   *(Hint: add the two cases, then subtract twice the overlap. Check n = 100 →
   33 + 20 − 2×6 = 41.)*
7. (Challenge) In [1, 100], how many integers are divisible by 2, 3, or 5?
   *(Hint: three-set inclusion–exclusion. Answer: 50 + 33 + 20 − 16 − 10 − 6 +
   3 = 74.)*
