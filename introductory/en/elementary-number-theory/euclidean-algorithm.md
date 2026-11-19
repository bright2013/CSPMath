# Euclidean Algorithm 【3】

辗转相除法（欧几里得算法）

## Description

The **greatest common divisor** gcd(a, b) is the largest positive integer dividing
both a and b. The **Euclidean algorithm** computes it by repeated division:

> gcd(a, b) = gcd(b, a mod b), until the remainder is 0; the last non-zero
> remainder is the GCD.

**Why it works**: if a = b·q + r, then every common divisor of a and b also divides
r = a − b·q, and every common divisor of b and r also divides a — so the pair
(a, b) and the pair (b, r) have exactly the same common divisors.

**Speed**: each two steps shrink the numbers by at least a factor of 2, so the
algorithm takes O(log min(a, b)) steps — instant even for 64-bit integers.

**Least common multiple**:

> lcm(a, b) = a · b / gcd(a, b)

Divide first (a / gcd(a, b) · b) to avoid overflow. In C++17 you also have
`std::__gcd(a, b)` (GNU) and `std::gcd`, `std::lcm` in `<numeric>`.

Two numbers with gcd(a, b) = 1 are called **coprime (互质)**.

## Examples

**Example 1.** gcd(252, 105):

```
252 = 105 × 2 + 42
105 =  42 × 2 + 21
 42 =  21 × 2 +  0   →  gcd = 21
```

**Example 2.** Reduce the fraction 252/105: divide both by gcd = 21 → 12/5.

**Example 3 (C++).** Recursive and iterative GCD:

```cpp
long long gcd(long long a, long long b) {
    return b == 0 ? a : gcd(b, a % b);
}

long long lcm(long long a, long long b) {
    return a / gcd(a, b) * b;   // divide first to avoid overflow
}
```

**Example 4.** lcm(12, 18) = 12 × 18 / gcd(12, 18) = 216 / 6 = 36.

**Example 5.** Are 35 and 12 coprime? gcd(35, 12) = gcd(12, 11) = gcd(11, 1) =
gcd(1, 0) = 1 → yes.

## Practice

1. Compute by hand with the Euclidean algorithm: gcd(1071, 462); gcd(240, 105).
   *(Answer: 21; 15.)*
2. Reduce the fraction 1071/462 to lowest terms. *(Answer: divide by 21 → 51/22.)*
3. Compute lcm(15, 20, 24). *(Hint: lcm is associative. Answer: 120.)*
4. Two gears have 48 and 36 teeth. After how many turns of the first gear do the
   contact points realign? *(Answer: lcm(48, 36) / 48 = 144 / 48 = 3 turns.)*
5. Write a program that reads n pairs (a, b) and prints gcd and lcm of each pair.
6. How many integers in [1, 100] are coprime with 36?
   *(Hint: 36 = 2²·3²; exclude multiples of 2 or 3 via inclusion–exclusion.
   Answer: 100 − 50 − 33 + 16 = 33.)*
7. (Challenge) Show that gcd(Fₙ, Fₙ₊₁) = 1 for consecutive Fibonacci numbers.
   *(Hint: gcd(Fₙ₊₁, Fₙ) = gcd(Fₙ, Fₙ₊₁ − Fₙ) = gcd(Fₙ, Fₙ₋₁).)*
