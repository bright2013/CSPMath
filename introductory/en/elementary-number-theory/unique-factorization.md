# Unique Factorization Theorem 【3】

整数唯一分解定理

## Description

**Fundamental theorem of arithmetic**: every integer n > 1 can be written as a
product of prime powers, and this factorization is **unique** up to the order of
the factors:

> n = p₁^a₁ · p₂^a₂ · … · pₖ^aₖ, where p₁ < p₂ < … < pₖ are primes and each aᵢ ≥ 1.

Example: 360 = 2³ · 3² · 5¹.

**Why it is useful.** From the factorization n = p₁^a₁ · … · pₖ^aₖ you get:

* **Number of positive divisors**: d(n) = (a₁+1)(a₂+1)…(aₖ+1).
* **Sum of positive divisors**: σ(n) = (1+p₁+…+p₁^a₁) · … · (1+pₖ+…+pₖ^aₖ).
* n is a **perfect square** ⇔ every aᵢ is even.
* **GCD/LCM via factorization**: take the min (resp. max) exponent of each prime.

**Factorization by trial division**: try divisors from 2 up to √n, dividing out each
prime factor as found. If anything greater than 1 remains at the end, it is itself a
prime factor. Runs in O(√n), fine for n up to about 10¹².

## Examples

**Example 1.** Factor 360: 360 = 2×180 = 2²×90 = 2³×45 = 2³×3²×5.

**Example 2.** Number of divisors of 360 = 2³·3²·5¹:
d(360) = (3+1)(2+1)(1+1) = 4 × 3 × 2 = 24.

**Example 3.** Is 720 a perfect square? 720 = 2⁴·3²·5¹ — the exponent of 5 is odd,
so no.

**Example 4 (C++).** Prime factorization by trial division:

```cpp
void factorize(long long n) {
    for (long long p = 2; p * p <= n; p++) {
        while (n % p == 0) {
            cout << p << " ";   // prime factor p
            n /= p;
        }
    }
    if (n > 1) cout << n;       // remaining prime factor
}
// factorize(360) prints: 2 2 2 3 3 5
```

**Example 5.** gcd(360, 252) by factorization:
360 = 2³·3²·5, 252 = 2²·3²·7 → gcd = 2²·3² = 36, lcm = 2³·3²·5·7 = 2520.

## Practice

1. Factor into primes: 84, 225, 1001, 2025.
   *(Answer: 2²·3·7; 3²·5²; 7·11·13; 3⁴·5².)*
2. How many positive divisors does 1000 = 2³·5³ have? *(Answer: 4×4 = 16.)*
3. Which of 144, 200, 576 are perfect squares? *(Answer: 144 = 12² and 576 = 24².)*
4. Find the smallest positive integer n with exactly 6 divisors.
   *(Hint: 6 = 6 or 6 = 2×3 → forms p⁵ or p¹q². Answer: 12 = 2²·3.)*
5. Compute gcd(840, 462) and lcm(840, 462) using prime factorizations.
   *(Answer: 840 = 2³·3·5·7, 462 = 2·3·7·11 → gcd = 42, lcm = 9240.)*
6. Write a program that reads n (n ≤ 10¹²) and prints its factorization in the
   form `p1^a1 * p2^a2 * ...`.
7. (Challenge) Sum of all positive divisors of 360: use the σ formula.
   *(Answer: (1+2+4+8)(1+3+9)(1+5) = 15 × 13 × 6 = 1170.)*
