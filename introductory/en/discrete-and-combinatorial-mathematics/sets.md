# Sets 【2】

集合

## Description

A **set (集合)** is a collection of **distinct** objects, called elements. Order does
not matter and duplicates are ignored: {1, 2, 2, 3} = {1, 2, 3} = {3, 2, 1}.

Core notions:

* **Membership**: a ∈ A ("a belongs to A"), a ∉ A ("a does not belong to A").
* **Subset**: A ⊆ B if every element of A is in B. The **empty set** ∅ is a subset of
  every set. A set with n elements has exactly 2ⁿ subsets.
* **Operations**:
  * union A ∪ B — elements in A or B (or both);
  * intersection A ∩ B — elements in both;
  * difference A ∖ B — elements in A but not in B;
  * complement Ā — elements of the universe U not in A.
* **Cardinality** |A|: the number of elements of a finite set.

**Inclusion–exclusion for two sets**:

> |A ∪ B| = |A| + |B| − |A ∩ B|

**In programming**, sets show up as "have we seen this value before?" — typically
implemented with a boolean array, `std::set`, or `std::unordered_set`.

## Examples

**Example 1.** A = {1, 2, 3, 4}, B = {3, 4, 5}. Then
A ∪ B = {1, 2, 3, 4, 5}, A ∩ B = {3, 4}, A ∖ B = {1, 2}, and |A| = 4.

**Example 2.** The set {a, b, c} has 2³ = 8 subsets:
∅, {a}, {b}, {c}, {a,b}, {a,c}, {b,c}, {a,b,c}.

**Example 3.** In a class of 40 students, 25 play basketball, 18 play football, and
10 play both. How many play at least one of the two?
|A ∪ B| = 25 + 18 − 10 = 33. So 40 − 33 = 7 play neither.

**Example 4 (C++).** Count distinct values in an array:

```cpp
#include <unordered_set>
unordered_set<int> s(a, a + n);
cout << s.size();   // number of distinct elements
```

**Example 5 (C++).** Membership test with a boolean array (values in [0, 10⁶]):

```cpp
vector<bool> seen(1000001, false);
seen[x] = true;            // insert
if (seen[y]) { ... }       // y ∈ set?
```

## Practice

1. Let A = {2, 4, 6, 8}, B = {4, 8, 12}. Find A ∪ B, A ∩ B, A ∖ B and |A ∪ B|.
   *(Answer: {2,4,6,8,12}; {4,8}; {2,6}; 5.)*
2. How many subsets does {1, 2, 3, 4, 5} have? How many of them are non-empty?
   *(Answer: 2⁵ = 32; 31.)*
3. Of 50 students, 30 like math, 26 like physics, 12 like both. How many like
   neither? *(Answer: 50 − (30 + 26 − 12) = 6.)*
4. True or false: ∅ ∈ {∅}? ∅ ⊆ {1, 2}? *(Answer: true; true.)*
5. In [1, 100], how many integers are divisible by 4 or by 6?
   *(Hint: multiples of 4 ∪ multiples of 6; note lcm(4,6) = 12.
   Answer: 25 + 16 − 8 = 33.)*
6. Write a program that reads n integers and prints how many distinct values appear
   and how many of them occur exactly once.
7. (Challenge) A = {x : x | 12}, B = {x : x | 18} (positive divisors). List A ∩ B
   and connect it to gcd(12, 18). *(Answer: {1, 2, 3, 6}; its maximum is the gcd.)*
