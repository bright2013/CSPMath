# Divisibility, Factors and Multiples 【3】

整除、因数、倍数、指数、质(素)数、合数

## Description

An integer a **divides** an integer b (written **a | b**) if there exists an integer
k such that b = a·k. In that case:

* a is a **factor (divisor, 因数)** of b,
* b is a **multiple (倍数)** of a,
* the remainder of b ÷ a is 0.

Useful properties of divisibility:

* If a | b and a | c, then a | (b ± c) and a | b·c.
* If a | b and b | c, then a | c (transitivity).
* If a | b and b | a, then |a| = |b|.

**Exponents (指数)**: aⁿ means a multiplied by itself n times. Laws you will use
constantly:

* aᵐ · aⁿ = aᵐ⁺ⁿ
* (aᵐ)ⁿ = aᵐⁿ
* a⁰ = 1 (a ≠ 0)

**Primes and composites:**

* A **prime number (质数/素数)** is an integer greater than 1 whose only positive
  factors are 1 and itself: 2, 3, 5, 7, 11, 13, …
* A **composite number (合数)** is an integer greater than 1 that is not prime, i.e.
  it has a factor other than 1 and itself.
* 1 is neither prime nor composite. 2 is the only even prime.

**Trial division test**: to check whether n is prime, it is enough to test divisors
up to √n — if n = a·b with a ≤ b, then a ≤ √n.

## Examples

**Example 1.** Does 7 divide 252? Yes: 252 = 7 × 36, so 7 | 252, 7 is a factor of
252, and 252 is a multiple of 7.

**Example 2.** List the positive factors of 36:
1, 2, 3, 4, 6, 9, 12, 18, 36 — nine factors in total.

**Example 3.** Is 97 prime? √97 < 10, so test 2, 3, 5, 7: none divides 97, hence 97
is prime.

**Example 4 (C++).** Count the multiples of k in [1, n]:

```cpp
long long n = 1000, k = 7;
cout << n / k;        // 142, because ⌊1000/7⌋ = 142
```

**Example 5 (C++).** Primality test by trial division, O(√n):

```cpp
bool isPrime(long long n) {
    if (n < 2) return false;
    for (long long i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}
```

## Practice

1. How many integers in [1, 500] are divisible by 6? *(Answer: ⌊500/6⌋ = 83.)*
2. Find all positive factors of 60. How many are there?
   *(Answer: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 — twelve.)*
3. Which of the following are prime: 51, 59, 87, 91, 101?
   *(Answer: 59 and 101; 51 = 3×17, 87 = 3×29, 91 = 7×13.)*
4. Compute 2¹⁰ and 3⁵ without a calculator. *(Answer: 1024 and 243.)*
5. Write a program that reads n and prints all its positive factors in O(√n) time.
   *(Hint: for each i ≤ √n with i | n, both i and n/i are factors.)*
6. How many integers in [1, 1000] are divisible by 3 or by 5?
   *(Hint: use inclusion–exclusion: ⌊1000/3⌋ + ⌊1000/5⌋ − ⌊1000/15⌋ = 467.)*
