# Bézout's Identity 【7】

裴蜀定理

## Description

**Bézout's identity (裴蜀定理)**: for any integers a, b (not both zero), there exist
integers x, y such that

> a·x + b·y = gcd(a, b)

Moreover, gcd(a, b) is the **smallest positive** integer expressible as a·x + b·y
with integer x, y.

**Why the smallest positive combination must be the gcd.** Every combination
a·x + b·y is divisible by gcd(a, b), since the gcd divides both terms — so no
combination can be smaller than gcd(a, b) (in absolute value, unless 0). Conversely,
running the Euclidean algorithm backwards shows gcd(a, b) itself *is* a combination
— that is exactly what the [extended Euclidean algorithm](extended-euclid.md)
computes.

**Immediate consequences:**

* a, b are coprime ⇔ there exist x, y with a·x + b·y = 1.
* The linear Diophantine equation a·x + b·y = c has integer solutions iff
  gcd(a, b) | c.
* The set {a·x + b·y : x, y ∈ ℤ} is exactly the set of multiples of gcd(a, b).
* Existence of modular inverses: a⁻¹ mod m exists iff gcd(a, m) = 1, because
  a·x ≡ 1 (mod m) is the same as a·x + m·y = 1.

## Examples

**Example 1.** a = 252, b = 105, gcd = 21. One Bézout pair: 252·(−2) + 105·5 =
−504 + 525 = 21. So x = −2, y = 5.

**Example 2.** 35 and 12 are coprime: 35·(−1) + 12·3 = 1 (x = −1, y = 3).

**Example 3.** Does 6x + 9y = 20 have integer solutions? gcd(6, 9) = 3 ∤ 20 → no.
And 6x + 9y = 21? 3 | 21 → yes: divide by 3 to get 2x + 3y = 7, one solution
x = 2, y = 1. ✓

**Example 4.** Frobenius coin problem (two denominations): with coins of 3 and 5,
every amount ≥ 8 is payable; 7 is not. Bézout guarantees all sufficiently large
multiples of gcd(3,5) = 1 are representable with *non-negative* combinations from
some point on — but it says nothing about small values, which must be checked by
hand.

**Example 5.** Water jug: jugs of 4 and 9 liters — can you measure exactly 6 liters?
Since gcd(4, 9) = 1 | 6, yes. Reading the combination 9·2 − 4·3 = 6 as an
algorithm: fill the 9-jug twice, emptying into the 4-jug (discarding when full)
three times.

## Practice

1. Find integers x, y with 30x + 21y = 3. *(Answer: x = −2, y = 3, since
   −60 + 63 = 3.)*
2. Which equations have integer solutions? 14x + 35y = 7; 14x + 35y = 10;
   8x + 18y = 2. *(Answer: yes; no (7 ∤ 10); yes (2 | 2).)*
3. Find one solution of 11x + 7y = 1, then describe all solutions.
   *(Answer: x = 2, y = −3; general x = 2 + 7t, y = −3 − 11t.)*
4. Show that consecutive integers are coprime using Bézout. *((n+1)·1 + n·(−1) = 1.)*
5. Two water jugs hold 12 and 17 liters. Can you measure 1 liter? 2 liters?
   Describe a strategy. *(Answer: yes, gcd = 1: 17·5 − 12·7 = 1; then repeat the
   1-liter cycle twice for 2.)*
6. What is the smallest positive value of 123x + 45y over integers x, y?
   *(Answer: gcd(123, 45) = 3.)*
7. (Challenge) Prove Bézout's identity from the Euclidean algorithm by working
   backwards through the divisions for (252, 105).
