# Elementary Number Theory (初等数论)

## Syllabus items

* 【3】Divisibility, factors, multiples, exponents, prime numbers, composite numbers
  (整除、因数、倍数、指数、质(素)数、合数)
* 【3】Floor/integer rounding (取整)
* 【3】Modular arithmetic and remainder (模运算与取余)
* 【3】Unique factorization theorem of integers (整数唯一分解定理)
* 【3】Euclidean algorithm (辗转相除法，欧几里得算法)
* 【4】Prime sieves: Sieve of Eratosthenes and linear sieve (素数筛法：埃氏筛法与线性筛法)

## Divisibility, factors and multiples 【3】

An integer a **divides** an integer b (written a | b) if b = a·k for some integer k.
Then a is a **factor (因数)** of b and b is a **multiple (倍数)** of a.

* A **prime (质数/素数)** is an integer greater than 1 whose only positive factors are
  1 and itself: 2, 3, 5, 7, 11, …
* A **composite number (合数)** is an integer greater than 1 that is not prime.
* **Exponents (指数)**: aⁿ means a multiplied by itself n times; laws such as
  aᵐ·aⁿ = aᵐ⁺ⁿ and (aᵐ)ⁿ = aᵐⁿ are used constantly.

## Floor and rounding 【3】

* **Floor (下取整)** ⌊x⌋: the greatest integer not exceeding x, e.g. ⌊3.7⌋ = 3, ⌊−2.3⌋ = −3.
* **Ceiling (上取整)** ⌈x⌉: the smallest integer not less than x, e.g. ⌈3.2⌉ = 4.
* In C++, integer division of non-negative integers truncates toward zero, which
  coincides with floor for non-negative values; take care with negative operands.

## Modular arithmetic 【3】

a mod m is the **remainder** when a is divided by m (m > 0), lying in 0 … m−1.

Basic identities:

* (a + b) mod m = ((a mod m) + (b mod m)) mod m
* (a − b) mod m = ((a mod m) − (b mod m) + m) mod m
* (a · b) mod m = ((a mod m) · (b mod m)) mod m

These keep intermediate values small and are essential in competitive programming.

## Unique factorization theorem 【3】

Every integer n > 1 can be written **uniquely** (up to ordering) as a product of
prime powers:

> n = p₁^a₁ · p₂^a₂ · … · pₖ^aₖ  (p₁ < p₂ < … < pₖ are primes)

Example: 360 = 2³ · 3² · 5. From the factorization, the number of positive divisors
is (a₁+1)(a₂+1)…(aₖ+1).

## Euclidean algorithm 【3】

Computes the greatest common divisor (GCD) by repeated division:

> gcd(a, b) = gcd(b, a mod b), stopping when the remainder is 0.

Example: gcd(252, 105) = gcd(105, 42) = gcd(42, 21) = gcd(21, 0) = 21.

It also gives the least common multiple: lcm(a, b) = a·b / gcd(a, b).

## Prime sieves 【4】

**Sieve of Eratosthenes (埃氏筛法)**: to find all primes up to n, mark off multiples of
each prime starting from p². Complexity O(n log log n).

**Linear sieve (线性筛法)**: every composite number is marked exactly once, by its
smallest prime factor. Complexity O(n), and it can simultaneously compute
multiplicative functions such as Euler's totient function φ.
