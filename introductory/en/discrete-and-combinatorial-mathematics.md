# Discrete and Combinatorial Mathematics (离散与组合数学)

## Syllabus items

* 【2】Sets (集合)
* 【2】Addition principle (加法原理)
* 【2】Multiplication principle (乘法原理)
* 【4】Permutations (排列)
* 【4】Combinations (组合)
* 【4】Pascal's (Yang Hui) triangle (杨辉三角)

## Sets 【2】

A **set (集合)** is a collection of distinct objects. Key notions:

* Membership: a ∈ A ("a belongs to A").
* Subset: A ⊆ B; empty set ∅.
* Operations: union A ∪ B, intersection A ∩ B, difference A ∖ B, complement.
* Cardinality |A|: the number of elements in a finite set.

## Addition principle 【2】

If a task can be done in one of several **mutually exclusive** cases, with n₁, n₂, …,
nₖ ways respectively, the total number of ways is:

> n₁ + n₂ + … + nₖ

Example: travel by one of 3 trains or one of 4 buses → 3 + 4 = 7 choices.

## Multiplication principle 【2】

If a task is completed in **steps**, with n₁ ways for step 1, n₂ ways for step 2, …,
the total number of ways is:

> n₁ · n₂ · … · nₖ

Example: 3 shirts and 4 pairs of trousers → 3 × 4 = 12 outfits.

## Permutations 【4】

An ordered arrangement of m elements chosen from n distinct elements:

> A(n, m) = n! / (n−m)!

Example: A(5, 3) = 5·4·3 = 60. A full permutation of n elements is n!.

## Combinations 【4】

An unordered selection of m elements from n distinct elements:

> C(n, m) = n! / (m! (n−m)!)

Properties: C(n, m) = C(n, n−m); C(n, m) = C(n−1, m−1) + C(n−1, m).

## Pascal's (Yang Hui) triangle 【4】

Row n of the triangle lists the binomial coefficients C(n, 0), C(n, 1), …, C(n, n).
Each interior entry is the sum of the two entries above it:

```
1
1  1
1  2  1
1  3  3  1
1  4  6  4  1
```

This encodes the recurrence C(n, m) = C(n−1, m−1) + C(n−1, m) and the binomial
theorem (a + b)ⁿ = Σ C(n, k) aⁿ⁻ᵏ bᵏ.
