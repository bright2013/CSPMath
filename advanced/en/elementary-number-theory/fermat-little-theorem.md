# Fermat's Little Theorem 【7】

费马小定理

## Description

**Fermat's little theorem**: if p is prime and p ∤ a, then

> a^(p−1) ≡ 1 (mod p)

Equivalent form valid for **all** a: aᵖ ≡ a (mod p).

It is Euler's theorem specialized to prime moduli, since φ(p) = p − 1.

**Main uses:**

* **Modular inverse** (see the dedicated page): a⁻¹ ≡ a^(p−2) (mod p) when p is
  prime and p ∤ a — computed by fast exponentiation in O(log p).
* **Exponent reduction**: aᵏ mod p = a^(k mod (p−1)) mod p when p ∤ a.
* **Primality testing**: if a^(n−1) ≢ 1 (mod n) for some a, then n is composite
  (the basis of the Fermat primality test; beware Carmichael numbers like 561,
  which fool it).

**Fast exponentiation (快速幂)**: compute aᵏ mod m in O(log k) by squaring:

## Examples

**Example 1.** 2⁶ = 64 ≡ 1 (mod 7). Also 3⁶ = 729 = 7·104 + 1 ≡ 1 (mod 7). ✓

**Example 2.** Compute 2¹⁰⁰ mod 11: 2¹⁰ ≡ 1 (mod 11), so 2¹⁰⁰ = (2¹⁰)¹⁰ ≡ 1.

**Example 3.** Inverse of 3 mod 7: 3⁵ = 243 = 7·34 + 5 ≡ 5 (mod 7). Check:
3·5 = 15 ≡ 1. ✓

**Example 4 (C++).** Fast exponentiation:

```cpp
long long qpow(long long a, long long k, long long m) {
    long long r = 1 % m;
    a %= m;
    while (k > 0) {
        if (k & 1) r = r * a % m;
        a = a * a % m;
        k >>= 1;
    }
    return r;
}
// inverse mod prime p: qpow(a, p - 2, p)
```

**Example 5.** 561 = 3 × 11 × 17 is composite, yet a⁵⁶⁰ ≡ 1 (mod 561) for every a
coprime to 561 — a Carmichael number; Fermat's test alone cannot detect it.

## Practice

1. Verify Fermat's little theorem for a = 4, p = 5. *(4⁴ = 256 ≡ 1 mod 5. ✓)*
2. Compute 5²⁰²⁵ mod 13. *(Hint: 5¹² ≡ 1; 2025 mod 12 = 9; 5⁹ mod 13. Answer: 5.)*
3. Find 7⁻¹ mod 11 using a^(p−2). *(Answer: 7⁹ mod 11 = 8; check 7·8 = 56 ≡ 1.)*
4. Compute the last digit of 2²⁰²⁵ via mod 10 cycles, then via mod 5 + Fermat and
   parity. *(Answer: 2.)*
5. Show 341 = 11 × 31 is a Fermat pseudoprime to base 2 (i.e. 2³⁴⁰ ≡ 1 mod 341)
   yet composite.
6. Implement `qpow` and verify (a·b) mod m equals qpow results for random cases;
   then compute 2^(10⁹) mod 1000000007. *(Answer: 140625001.)*
7. (Challenge) Using Fermat, prove that for prime p > 3, p | (1^(p−1) + 2^(p−1) +
   … + (p−1)^(p−1) − (p−1))… simpler: prove p | aᵖ − a for every integer a.
   *(Hint: aᵖ ≡ a (mod p) is exactly the claim; prove it by induction on a.)*
