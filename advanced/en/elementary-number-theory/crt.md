# Chinese Remainder Theorem 【7】

中国剩余定理

## Description

**Chinese remainder theorem (CRT)**: if m₁, m₂, …, mₖ are **pairwise coprime**
positive integers, then the system

> x ≡ a₁ (mod m₁)
> x ≡ a₂ (mod m₂)
> …
> x ≡ aₖ (mod mₖ)

has a **unique solution modulo M = m₁·m₂·…·mₖ**.

**Construction**: let Mᵢ = M / mᵢ and tᵢ = Mᵢ⁻¹ (mod mᵢ) (exists because
gcd(Mᵢ, mᵢ) = 1). Then:

> x ≡ Σᵢ aᵢ · Mᵢ · tᵢ (mod M)

**Why it matters**: it lets you work modulo several small coprime moduli instead of
one huge modulus — results mod M are reconstructed at the end. It also explains the
structure of the ring ℤ/Mℤ ≅ ℤ/m₁ℤ × … × ℤ/mₖℤ.

**Non-coprime moduli**: the system is solvable iff aᵢ ≡ aⱼ (mod gcd(mᵢ, mⱼ)) for
all pairs; the general merge uses exGCD.

## Examples

**Example 1 (classic).** 今有物不知其数：x ≡ 2 (mod 3), x ≡ 3 (mod 5),
x ≡ 2 (mod 7). Here M = 105, M₁ = 35, M₂ = 21, M₃ = 15;
t₁ = 35⁻¹ mod 3 = 2, t₂ = 21⁻¹ mod 5 = 1, t₃ = 15⁻¹ mod 7 = 1.

> x ≡ 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233 ≡ 23 (mod 105)

Check: 23 mod 3 = 2, mod 5 = 3, mod 7 = 2. ✓

**Example 2.** Solve x ≡ 1 (mod 4), x ≡ 2 (mod 9). M = 36, M₁ = 9, t₁ = 9⁻¹ mod 4 =
1; M₂ = 4, t₂ = 4⁻¹ mod 9 = 7 (4·7 = 28 ≡ 1). x ≡ 1·9·1 + 2·4·7 = 9 + 56 = 65 ≡
29 (mod 36). Check: 29 mod 4 = 1, 29 mod 9 = 2. ✓

**Example 3 (C++).** CRT for two coprime moduli:

```cpp
// solve x ≡ a1 (mod m1), x ≡ a2 (mod m2), gcd(m1, m2) = 1
long long x1, y1;
exgcd(m1, m2, x1, y1);                    // m1·x1 + m2·y1 = 1
long long x = (a1 + (a2 - a1) % m2 * x1 % m2 * m1) % (m1 * m2);
x = (x + m1 * m2) % (m1 * m2);
```

**Example 4.** Garner's algorithm restores x from residues without big-int
arithmetic — useful when M overflows 64 bits.

## Practice

1. Solve x ≡ 1 (mod 3), x ≡ 2 (mod 5). *(Answer: x ≡ 7 (mod 15).)*
2. Solve x ≡ 2 (mod 5), x ≡ 3 (mod 7), x ≡ 1 (mod 8).
   *(Answer: M = 280; M₁ = 56, t₁ = 56⁻¹ mod 5 = 1; M₂ = 40, t₂ = 40⁻¹ mod 7 =
   5⁻¹ mod 7 = 3; M₃ = 35, t₃ = 35⁻¹ mod 8 = 3⁻¹ mod 8 = 3.
   x ≡ 2·56·1 + 3·40·3 + 1·35·3 = 112 + 360 + 105 = 577 ≡ 17 (mod 280).
   Check: 17 mod 5 = 2, 17 mod 7 = 3, 17 mod 8 = 1. ✓)*
3. Find the smallest positive x with x ≡ 4 (mod 6), x ≡ 3 (mod 7).
   *(gcd(6, 7) = 1, so CRT applies. Answer: x = 10; solutions are x ≡ 10 (mod 42).)*
4. Is x ≡ 1 (mod 4), x ≡ 3 (mod 6) solvable? *(gcd(4, 6) = 2 and 1 ≡ 3 (mod 2),
   so yes. Candidates x ≡ 3 (mod 6) are 3, 9, 15, …; x = 9 satisfies x ≡ 1 (mod 4).
   Answer: x ≡ 9 (mod 12).)*
5. Implement CRT for k pairwise-coprime congruences and test on Examples 1–2.
6. (Challenge) Show CRT for two moduli directly: x = a₁ + m₁·t, substitute into the
   second congruence and solve for t using the inverse of m₁ mod m₂.
