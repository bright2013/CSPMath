# Prime Sieves 【4】

素数筛法：埃氏筛法与线性筛法

## Description

**Task**: find all prime numbers in [1, n] (typically n up to 10⁶–10⁷).

### Sieve of Eratosthenes (埃氏筛法)

Idea: start with everything marked as prime; for each prime p, cross out all its
multiples p², p²+p, p²+2p, … (multiples below p² were already crossed out by
smaller primes).

* Time complexity: **O(n log log n)** — fast enough for n = 10⁷.
* Memory: a boolean array of size n+1.

### Linear sieve (线性筛法 / Euler sieve)

Idea: maintain a list of primes found so far; for each integer i, mark i·p for
each prime p **up to the smallest prime factor of i**, then stop. Every composite
is crossed out **exactly once**, by its smallest prime factor.

* Time complexity: **O(n)** — truly linear.
* Bonus: the same loop can compute multiplicative functions (e.g. Euler's totient
  φ, divisor counts) for free — this becomes important at higher levels.

### Which to use at 入门级?

Eratosthenes is simpler to write and remember; learn it first. The linear sieve is
one difficulty level higher 【4】 but is the standard tool in serious contests.

## Examples

**Example 1.** Primes up to 30 by Eratosthenes:
cross out multiples of 2 (from 4), of 3 (from 9), of 5 (from 25);
7² = 49 > 30 so we stop. Remaining primes:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

**Example 2 (C++).** Sieve of Eratosthenes:

```cpp
vector<bool> isPrime(n + 1, true);
isPrime[0] = isPrime[1] = false;
for (int p = 2; (long long)p * p <= n; p++)
    if (isPrime[p])
        for (int j = p * p; j <= n; j += p)
            isPrime[j] = false;
```

**Example 3 (C++).** Linear sieve:

```cpp
vector<int> primes;
vector<bool> vis(n + 1, false);
for (int i = 2; i <= n; i++) {
    if (!vis[i]) primes.push_back(i);
    for (int p : primes) {
        if ((long long)i * p > n) break;
        vis[i * p] = true;
        if (i % p == 0) break;   // p is the smallest prime factor of i
    }
}
```

**Example 4.** In the linear sieve, why does `if (i % p == 0) break;` guarantee
each composite is marked once? Because it ensures i·p is marked with p as its
smallest prime factor; continuing past that point would mark i·p with a larger
prime while its true smallest prime factor is p — and it would then be re-marked
later, breaking linearity.

## Practice

1. List all primes up to 50 by hand with the Sieve of Eratosthenes.
   *(Answer: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.)*
2. How many primes are there below 100? *(Answer: 25.)*
3. Why is it enough to start crossing out from p² instead of 2p?
   *(Answer: every composite multiple k·p with k < p has a smaller prime factor and
   was already crossed out.)*
4. Implement the Eratosthenes sieve; read n (n ≤ 10⁷) and print the number of
   primes ≤ n. Measure the running time for n = 10⁷.
5. Implement the linear sieve and verify it prints the same prime count as your
   Eratosthenes sieve for n = 10⁶.
6. A **twin prime** is a pair (p, p+2) of primes, like (11, 13). Write a program
   that counts twin prime pairs with both members ≤ n. For n = 100 the answer is 8:
   (3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73).
7. (Challenge) Modify the linear sieve to also compute, for every i ≤ n, its
   smallest prime factor.
