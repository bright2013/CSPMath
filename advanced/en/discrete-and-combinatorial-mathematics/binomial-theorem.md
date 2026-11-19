# Binomial Theorem 【6】

二项式定理

## Description

**Binomial theorem**: for any non-negative integer n,

> (a + b)ⁿ = Σₖ₌₀ⁿ C(n, k) · aⁿ⁻ᵏ · bᵏ

The coefficients C(n, k) are exactly the entries of row n of **Pascal's (Yang Hui)
triangle** (see the Introductory Level space).

**Useful corollaries:**

* a = b = 1: Σₖ C(n, k) = 2ⁿ.
* a = 1, b = −1: Σₖ (−1)ᵏ C(n, k) = 0 (n ≥ 1) — even and odd subsets balance.
* Coefficient extraction: the coefficient of xᵏ in (1 + x)ⁿ is C(n, k).
* Approximation: (1 + x)ⁿ ≈ 1 + nx for small |x| (first two terms).

**Why combinatorial**: (a + b)ⁿ is a product of n factors; choosing b from k of
them (and a from the rest) can be done in C(n, k) ways — each term aⁿ⁻ᵏbᵏ appears
exactly C(n, k) times.

**In contests**: binomial expansions modulo a prime (with precomputed factorials and
inverse factorials) are everywhere — polynomial identities, expected values,
generating-function manipulations.

## Examples

**Example 1.** (x + 2)⁴ = x⁴ + 4·2x³ + 6·4x² + 4·8x + 16 =
x⁴ + 8x³ + 24x² + 32x + 16.

**Example 2.** Coefficient of x³ in (2x + 1)⁵: C(5, 3)·(2x)³·1² = 10·8x³ → 80.

**Example 3.** Σₖ C(10, k) = 2¹⁰ = 1024; Σₖ (−1)ᵏC(10, k) = 0 →
C(10,0)+C(10,2)+… = C(10,1)+C(10,3)+… = 512.

**Example 4.** 99⁴ = (100 − 1)⁴ = 10⁸ − 4·10⁶ + 6·10⁴ − 400 + 1 = 96 059 601.

**Example 5 (C++).** Coefficient of xᵏ in (1 + x)ⁿ mod p:

```cpp
// = C(n, k) mod p, with precomputed factorials:
long long coef = fact[n] * invFact[k] % P * invFact[n - k] % P;
```

**Example 6.** Number of odd entries in row n of Pascal's triangle is
2^(popcount(n)) (Lucas' theorem corollary — NOI-level flavor, stated here for
intuition).

## Practice

1. Expand (x + 3)³ and (a − b)⁴.
   *(Answer: x³ + 9x² + 27x + 27; a⁴ − 4a³b + 6a²b² − 4ab³ + b⁴.)*
2. Find the coefficient of x⁵ in (1 + x)⁸; of x²y³ in (2x + y)⁵.
   *(Answer: 56; C(5,2)·4·… = 10·4 = 40? Compute: C(5,2)(2x)²y³ = 10·4 = 40x²y³.
   Answer: 40.)*
3. Compute Σₖ k·C(n, k) for n = 4 by hand; guess and prove the general formula.
   *(Answer: n·2ⁿ⁻¹; differentiate (1+x)ⁿ at x = 1.)*
4. Show 11ⁿ ≡ 1 (mod 10) using the binomial theorem on (10 + 1)ⁿ.
5. Approximate 1.02¹⁰ to two decimal places using the first three terms.
   *(Answer: 1 + 0.2 + 45·0.0004 = 1.218 → 1.22.)*
6. Compute C(50, 25) mod 998244353 with a program using factorials and inverse
   factorials. *(Answer: 402302378… let the program tell you.)*
7. (Challenge) Prove Σₖ C(m, k)·C(n, r−k) = C(m+n, r) (Vandermonde's identity) by
   comparing coefficients in (1+x)ᵐ(1+x)ⁿ = (1+x)ᵐ⁺ⁿ.
