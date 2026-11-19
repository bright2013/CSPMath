# Euler's Theorem and Totient Function 【7】

欧拉定理和欧拉函数

## Description

**Euler's totient function** φ(n) counts the integers in [1, n] that are coprime
with n.

**Computation from the prime factorization** n = p₁^a₁ · … · pₖ^aₖ:

> φ(n) = n · ∏ᵢ (1 − 1/pᵢ) = n · (p₁−1)/p₁ · … · (pₖ−1)/pₖ

Special cases: φ(p) = p − 1 for prime p; φ(pᵏ) = pᵏ − pᵏ⁻¹; and φ is
**multiplicative**: φ(ab) = φ(a)φ(b) when gcd(a, b) = 1.

**Euler's theorem**: if gcd(a, n) = 1, then

> a^φ(n) ≡ 1 (mod n)

Consequence: to compute aᵏ mod n with gcd(a, n) = 1, you may reduce the exponent
mod φ(n): aᵏ ≡ a^(k mod φ(n)) (mod n).

**Computing φ for all i ≤ n** can be done in the linear sieve in O(n).

## Examples

**Example 1.** φ(12): numbers coprime with 12 in [1,12] are 1, 5, 7, 11 → φ(12) = 4.
Formula check: 12 = 2²·3, φ(12) = 12·(1/2)·(2/3) = 4. ✓

**Example 2.** φ(36) = 36·(1/2)·(2/3) = 12. φ(100) = 100·(1/2)·(4/5) = 40.

**Example 3.** Euler's theorem with a = 5, n = 12: 5⁴ = 625 = 12·52 + 1 ≡ 1 (mod 12). ✓

**Example 4.** Last two digits of 7²⁰²⁴: gcd(7, 100) = 1 and φ(100) = 40, so
7⁴⁰ ≡ 1 (mod 100); 2024 mod 40 = 24; 7²⁴ mod 100 = 01 → answer 01.
(Working: 7² = 49, 7⁴ = 01 (mod 100)! So actually 7²⁴ = (7⁴)⁶ ≡ 1.)

**Example 5 (C++).** φ(n) in O(√n) from trial division:

```cpp
long long phi(long long n) {
    long long r = n;
    for (long long p = 2; p * p <= n; p++)
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            r = r / p * (p - 1);
        }
    if (n > 1) r = r / n * (n - 1);
    return r;
}
```

**Example 6 (C++).** All φ(i) for i ≤ n in the linear sieve:

```cpp
phi[1] = 1;
for (int i = 2; i <= n; i++) {
    if (!vis[i]) { primes.push_back(i); phi[i] = i - 1; }
    for (int p : primes) {
        if ((long long)i * p > n) break;
        vis[i * p] = true;
        if (i % p == 0) { phi[i * p] = phi[i] * p; break; }
        phi[i * p] = phi[i] * (p - 1);
    }
}
```

## Practice

1. Compute φ(17), φ(24), φ(72), φ(1000). *(Answer: 16; 8; 24; 400.)*
2. Verify Euler's theorem for a = 2, n = 15 by direct computation.
   *(φ(15) = 8; 2⁸ = 256 = 15·17 + 1. ✓)*
3. Find the last digit of 3⁹⁹⁹. *(Hint: φ(10) = 4; 999 mod 4 = 3. Answer: 7.)*
4. Find the last two digits of 2²⁰²⁵. *(Careful: gcd(2, 100) ≠ 1, so Euler does not
   apply directly — compute the cycle of 2ⁿ mod 100 from n ≥ 2: period 20.
   Answer: 32.)*
5. Show Σ_{d | n} φ(d) = n for n = 12 by listing.
   *(φ(1)+φ(2)+φ(3)+φ(4)+φ(6)+φ(12) = 1+1+2+2+2+4 = 12.)*
6. Write a program computing φ(n) for a single n ≤ 10¹², and another computing
   φ(1)…φ(10⁷) with the linear sieve; compare runtimes.
7. (Challenge) How many fractions a/n with 1 ≤ a ≤ n are in lowest terms? What does
   this say about φ? *(Answer: φ(n) by definition.)*
