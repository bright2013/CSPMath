# Pigeonhole Principle 【6】

鸽巢原理

## Description

**Pigeonhole principle (drawer principle)**: if n + 1 or more pigeons are placed
into n holes, some hole contains at least two pigeons.

**Generalized form**: if N objects are placed into k boxes, some box contains at
least **⌈N/k⌉** objects.

The principle only proves *existence* — it never tells you *which* box. The art is
choosing what plays the role of pigeons and what the role of holes.

**Typical uses in contests**: "show that two of these numbers have the same …",
existence of a repeated value, subsequence with a sum divisible by n, etc.

## Examples

**Example 1.** Among any 13 people, two share a birth month. (13 pigeons, 12
months.)

**Example 2.** Among any 367 people, two share a birthday (366 possible birthdays
including Feb 29).

**Example 3.** Any 5 points inside an equilateral triangle of side 2: two are within
distance 1. Split the triangle into 4 sub-triangles of side 1 (the holes); two
points land in the same one.

**Example 4.** Among any n + 1 integers, two have the same residue mod n — their
difference is divisible by n.

**Example 5.** Given any 10 distinct two-digit numbers, there are two disjoint
non-empty subsets with equal sums. Pigeons: the 2¹⁰ − 1 = 1023 non-empty subsets;
holes: possible sums, from 10 to 10·99 = 990. 1023 > 990, so two subsets share a
sum; remove their common part to make them disjoint.

**Example 6 (classic).** Any sequence of n numbers contains a contiguous subsequence
whose sum is divisible by n: consider prefix sums s₀, s₁, …, sₙ mod n — n+1 pigeons,
n residues; either some sᵢ ≡ 0, or two prefix sums collide: sⱼ − sᵢ ≡ 0.

## Practice

1. How many socks must you draw blindfolded from a drawer with 4 colors to guarantee
   a matching pair? *(Answer: 5.)*
2. Show that among any 5 integers, some 3 have a sum divisible by 3.
   *(Hint: residues mod 3; either all three residues appear or one appears 3 times.)*
3. 51 points are placed in a square of side 7. Show some 3 lie within a circle of
   radius… simpler version: show two are within distance √2. *(Hint: split into 25
   cells of side 7/5… standard version: side 1 square, ⌈51/25⌉… use 5×5 grid: two
   points in a cell of diagonal √2/5.)*
4. Show that some positive multiple of 2025 consists only of digits 0 and 1.
   *(Hint: consider 1, 11, 111, … mod 2025 — 2026 pigeons, 2025 holes.)*
5. Prove: at any party of 6 people, some 3 are pairwise acquainted or pairwise
   unacquainted (Ramsey R(3,3) = 6). *(Hint: fix one person; 5 others split into
   acquainted/unacquainted — one group has ≥ 3.)*
6. Write a program that, given n and an array of n integers, finds a contiguous
   subsequence with sum divisible by n using prefix sums mod n.
7. (Challenge) Among any 52 integers, two exist whose sum **or** difference is
   divisible by 100. *(Hint: holes = residue pairs {i, 100−i}, 51 holes.)*
