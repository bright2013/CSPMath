# Floor and Integer Rounding 【3】

取整

## Description

* **Floor (下取整)** ⌊x⌋: the greatest integer not exceeding x.
  ⌊3.7⌋ = 3, ⌊5⌋ = 5, ⌊−2.3⌋ = −3 (note: −3, not −2!).
* **Ceiling (上取整)** ⌈x⌉: the smallest integer not less than x.
  ⌈3.2⌉ = 4, ⌈5⌉ = 5, ⌈−2.3⌉ = −2.
* **Round half up (四舍五入)**: the nearest integer, halves rounded away from zero:
  round(3.5) = 4, round(3.4) = 3.

A key identity: for any real x, ⌊x⌋ ≤ x < ⌊x⌋ + 1, and x − 1 < ⌈x⌉ ≤ x.

**In C++:** the `/` operator on integers **truncates toward zero**:

* 7 / 2 = 3 (= ⌊3.5⌋) — same as floor for non-negative operands;
* −7 / 2 = −3, but ⌊−3.5⌋ = −4 — different for negative operands!

So integer division coincides with floor only when the operands are non-negative.
Be careful whenever negative values can appear.

Handy formulas (a, b positive integers):

* Number of full groups of size b in a: a / b = ⌊a/b⌋.
* Groups needed to hold a items with capacity b: ⌈a/b⌉ = (a + b − 1) / b.

## Examples

**Example 1.** ⌊7/2⌋ = 3, ⌈7/2⌉ = 4. With n = 7 candies and boxes of 2, we fill
3 boxes and need 4 boxes to pack everything.

**Example 2.** Rounding in C++:

```cpp
#include <cmath>
floor(3.7);    // 3
floor(-2.3);   // -4
ceil(3.2);     // 4
round(3.5);    // 4
-7 / 2;        // -3  (truncation toward zero, NOT floor)
```

**Example 3.** Ceil division with positive integers:

```cpp
long long pages = (n + perPage - 1) / perPage;   // ⌈n / perPage⌉
```

**Example 4.** How many multiples of 4 lie in [10, 50]?
⌊50/4⌋ − ⌊9/4⌋ = 12 − 2 = 10.

## Practice

1. Compute: ⌊11/3⌋, ⌈11/3⌉, ⌊−11/3⌋, ⌈−11/3⌉.
   *(Answer: 3, 4, −4, −3.)*
2. In C++, what are 9 / 4, −9 / 4, 9 / −4? *(Answer: 2, −2, −2.)*
3. A bus seats 45 people. How many buses are needed for 200 students? Write the
   one-line C++ expression. *(Answer: (200 + 45 − 1) / 45 = 5.)*
4. How many integers in [1, 1000] are divisible by 8? *(Answer: ⌊1000/8⌋ = 125.)*
5. Prove or use: ⌈a/b⌉ = ⌊(a + b − 1)/b⌋ for positive integers a, b. Verify it for
   a = 10, b = 4 and a = 12, b = 4.
6. Write a program that reads a real number x and prints ⌊x⌋, ⌈x⌉ and round(x) on
   one line. Test it with x = −2.5.
