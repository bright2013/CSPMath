# Modular Inverse 【7】

模运算意义下的逆元

## Description

The **modular inverse** of a modulo m is an integer x such that

> a·x ≡ 1 (mod m)

written a⁻¹ (mod m). **It exists if and only if gcd(a, m) = 1**, and is then unique
modulo m.

**Existence, in one line**: a·x ≡ 1 (mod m) means a·x + m·y = 1 for some y — a
[Bézout equation](bezout.md), solvable exactly when gcd(a, m) = 1.

The inverse makes **division possible in modular arithmetic**: "divide by a" becomes
"multiply by a⁻¹":

> b / a (mod m) ≡ b · a⁻¹ (mod m)

This is what was missing at the introductory level, where only +, −, × respected
congruences.

**Three ways to compute it:**

1. **Extended Euclidean algorithm** — works for any modulus m with gcd(a, m) = 1:
   solve a·x + m·y = 1; then x ≡ a⁻¹ (mod m). O(log m).
2. **Fermat's little theorem** — when m = p is prime: a⁻¹ ≡ a^(p−2) (mod p), via
   fast exponentiation. O(log p).
3. **Linear preprocessing of all inverses mod prime p** (递推):
   inv[i] = (p − p/i) · inv[p % i] % p, giving inv[1..n] in O(n) total — the choice
   when a solution needs *every* inverse up to n.

**Typical use**: computing C(n, m) mod p — precompute factorials and inverse
factorials, then C(n,m) = fact[n] · invFact[m] · invFact[n−m] mod p.

## Examples

**Example 1.** 3⁻¹ mod 7 = 5, because 3·5 = 15 ≡ 1 (mod 7).

**Example 2.** Compute 1/2 + 1/3 (mod 7): 2⁻¹ = 4, 3⁻¹ = 5 → 4 + 5 = 9 ≡ 2 (mod 7).
Check: 1/2 + 1/3 = 5/6; 5·6⁻¹ = 5·6 = 30 ≡ 2. ✓ (6 is self-inverse mod 7.)

**Example 3.** 6⁻¹ mod 9 does not exist: gcd(6, 9) = 3 ≠ 1 (6x ≡ 1 (mod 9) would
need 3 | 1).

**Example 4 (C++).** Inverse mod prime via fast power, and the O(n) table:

```cpp
long long inv(long long a, long long p) { return qpow(a, p - 2, p); }

// all inverses mod prime p in O(n):
inv[1] = 1;
for (int i = 2; i <= n; i++)
    inv[i] = (p - p / i) * inv[p % i] % p;
```

**Example 5 (C++).** C(n, m) mod 998244353 with factorials:

```cpp
fact[0] = 1;
for (int i = 1; i <= N; i++) fact[i] = fact[i-1] * i % P;
invFact[N] = qpow(fact[N], P - 2, P);
for (int i = N; i >= 1; i--) invFact[i-1] = invFact[i] * i % P;
// C(n, m) = fact[n] * invFact[m] % P * invFact[n-m] % P
```

Note the trick: one exponentiation for invFact[N], then a downward pass turns it
into *all* inverse factorials — n inverses for the price of one.

## Practice

1. Find by hand: 2⁻¹ mod 5; 5⁻¹ mod 7; 10⁻¹ mod 13; 7⁻¹ mod 12.
   *(Answer: 3; 3; 4; 7.)*
2. Which have inverses: 4 mod 9, 6 mod 15, 11 mod 26? *(Answer: yes; no; yes.)*
3. Compute 5/3 mod 11 (i.e. 5·3⁻¹ mod 11). *(Answer: 3⁻¹ = 4, so 20 ≡ 9.)*
4. Using Fermat, compute 2⁻¹ mod 1000000007. *(Answer: 500000004 = (p+1)/2.)*
5. Verify the O(n) recurrence inv[i] = (p − p/i)·inv[p%i] % p for p = 7, i = 1…6 by
   comparing with brute force.
6. Implement C(n, m) mod 998244353 for n up to 10⁶ and answer q queries.
7. (Challenge) Prove the recurrence: write p = q·i + r with r = p mod i, so
   q·i + r ≡ 0 (mod p), hence i⁻¹ ≡ −q·r⁻¹ (mod p).
