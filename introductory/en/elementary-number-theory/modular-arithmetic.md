# Modular Arithmetic and Remainder 【3】

模运算与取余

## Description

For a positive integer m, **a mod m** is the remainder when a is divided by m; it
always lies in 0, 1, …, m−1. We say a and b are **congruent modulo m**, written

> a ≡ b (mod m),

when a and b leave the same remainder, i.e. m | (a − b).

**Basic identities** (the heart of modular arithmetic):

* (a + b) mod m = ((a mod m) + (b mod m)) mod m
* (a − b) mod m = ((a mod m) − (b mod m) + m) mod m
* (a · b) mod m = ((a mod m) · (b mod m)) mod m

Why they matter: in contests you often need "the answer mod 10⁹+7" etc. Applying
mod at **every step** keeps intermediate values small and avoids overflow. Note
there is **no** analogous identity for division at this level — division modulo m
needs modular inverses (提高级 content).

**C++ caveat**: `%` is a *remainder* operation whose result takes the sign of the
dividend: −7 % 3 = −1. To get a true residue in [0, m), write
`((a % m) + m) % m`.

**Cyclic reasoning**: mod m reduces problems to a cycle of length m — weekdays
(mod 7), hours (mod 12/24), last digits (mod 10), parity (mod 2).

## Examples

**Example 1.** 38 mod 5 = 3, because 38 = 5 × 7 + 3. And 13 ≡ 38 (mod 5) since
both leave remainder 3.

**Example 2.** Compute (97 × 86) mod 7 without big numbers:
97 mod 7 = 6, 86 mod 7 = 2, so (97 × 86) mod 7 = (6 × 2) mod 7 = 12 mod 7 = 5.

**Example 3.** The last digit of 7²⁰²⁴: powers of 7 mod 10 cycle
7, 9, 3, 1, 7, … with period 4. Since 2024 mod 4 = 0, the last digit is 1.

**Example 4 (C++).** Sum of n numbers modulo 1000000007 without overflow:

```cpp
const long long MOD = 1000000007;
long long sum = 0, x;
for (int i = 0; i < n; i++) {
    cin >> x;
    sum = (sum + x % MOD) % MOD;   // mod at every step
}
```

**Example 5 (C++).** Safe residue of a possibly negative value:

```cpp
long long r = ((a % m) + m) % m;   // always in [0, m)
```

## Practice

1. Compute: 100 mod 7; 2¹⁰ mod 5; (25 × 13 + 7) mod 11.
   *(Answer: 2; 1024 mod 5 = 4; 332 mod 11 = 2.)*
2. What is the last digit of 3²⁰²⁵? *(Hint: powers of 3 mod 10 cycle 3, 9, 7, 1.
   Answer: 3.)*
3. Today is Monday. What day of the week is it in 100 days?
   *(Answer: 100 mod 7 = 2 → Wednesday.)*
4. In C++, evaluate −13 % 5, then compute the true residue of −13 modulo 5.
   *(Answer: −3; true residue 2.)*
5. Compute (123456789 × 987654321) mod 100 by hand. *(Answer: (89 × 21) mod 100 =
   1869 mod 100 = 69.)*
6. Write a program that reads n and prints the last two digits of n!
   for n ≤ 20. *(Hint: keep only (result × i) mod 100 at each step; note the answer
   stabilizes at 00 from n = 10 onward.)*
