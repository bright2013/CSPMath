# Algebra (Senior High School) 【5】

代数（高中部分）

## Description

The senior-high algebra assumed by the syllabus covers seven blocks. You do not
need to re-derive theory here — you need *fluency*, because these tools appear
inside larger algorithmic problems (complexity analysis, expected values,
closed-form sums in DP, geometry formulas).

* **Sets and logic (集合与常用逻辑用语)**: union, intersection, complement;
  sufficient vs. necessary conditions. In problem statements, "A is a sufficient
  condition for B" means A ⇒ B; "necessary" means B ⇒ A. Mixing these up is the
  most common logic error in proofs.
* **Functions (函数)**: domain, range, monotonicity, parity; exponential functions
  (指数函数), logarithmic functions (对数函数) and power functions (幂函数);
  transformations (shifts, stretches, reflections); zeros and the bisection
  method. Bisection is the conceptual grandfather of binary search: a continuous
  function with f(l)·f(r) < 0 has a root in (l, r) — halve the interval until
  the precision suffices.
* **Sequences (数列)**: arithmetic aₙ = a₁ + (n−1)d, sum Sₙ = n(a₁+aₙ)/2;
  geometric aₙ = a₁qⁿ⁻¹, sum Sₙ = a₁(qⁿ−1)/(q−1) for q ≠ 1. These two sums are
  the backbone of complexity analysis: an arithmetic sum is O(n²), a geometric
  sum is dominated by its largest term (why binary exponentiation is O(log n) and
  why a doubling loop does 1+2+4+…+n < 2n work total).
* **Summation techniques**: 错位相减 (shift-and-subtract, for Σ of
  arithmetic×geometric terms) and 裂项相消 (telescoping, writing each term as
  f(k) − f(k+1)).
* **Trigonometry (三角函数)**: radian measure; sin, cos, tan and their graphs;
  identities (sin²x + cos²x = 1, sum/difference, double-angle); law of sines
  a/sin A = 2R and law of cosines c² = a² + b² − 2ab·cos C. In computational
  geometry the law of cosines is what connects side lengths to angles.
* **Inequalities (不等式)**: quadratic inequalities (solve via the parabola's
  sign); AM–GM (a + b)/2 ≥ √(ab) for a, b > 0, equality iff a = b; basic linear
  programming. AM–GM generalizes: (x₁+…+xₙ)/n ≥ (x₁…xₙ)^(1/n).
* **Complex numbers (复数)**: a + bi, arithmetic, modulus |a+bi| = √(a²+b²),
  conjugate; the complex plane. Multiplication adds angles and multiplies moduli
  — the seed of rotation formulas and (later) FFT.
* **Derivatives (导数, basic)**: f′(x) as rate of change; derivatives of xⁿ, eˣ,
  ln x; f′ > 0 ⇒ increasing. Use derivatives to find extrema of single-variable
  cost functions — often the fastest way to optimize a closed-form answer.

**When each tool fires in contests**: loops with i doubling → geometric series;
nested loops 1..n, 1..i → arithmetic series; "minimize perimeter for fixed area"
→ AM–GM; "find x with f(x) = 0, f continuous" → bisection.

## Examples

**Example 1.** Arithmetic sequence with a₁ = 3, d = 4: a₁₀ = 3 + 9·4 = 39,
S₁₀ = 10·(3+39)/2 = 210.

**Example 2.** Geometric series: 1 + 2 + 4 + … + 2ⁿ = 2ⁿ⁺¹ − 1. This is why
binary numbers and doubling loops behave the way they do: a binary counter
incrementing from 0 to n does fewer than 2n bit flips in total.

**Example 3.** AM–GM: for x > 0, x + 1/x ≥ 2, with equality at x = 1.

**Example 4.** Telescoping sum (裂项): Σₖ 1/(k(k+1)) = Σₖ (1/k − 1/(k+1)) =
1 − 1/(n+1) = n/(n+1). Recognize the pattern 1/(k(k+1)) = 1/k − 1/(k+1) — every
partial-fraction style identity invites telescoping.

**Example 5.** 错位相减: S = Σₖ₌₁ⁿ k·2ᵏ. Compute 2S = Σ k·2ᵏ⁺¹ and subtract:
S − 2S = Σ 2ᵏ − n·2ⁿ⁺¹ → S = (n−1)·2ⁿ⁺¹ + 2.

**Example 6.** cos 60° = 1/2; by the law of cosines, a triangle with sides
b = 3, c = 4 enclosing angle A = 60° has a² = 9 + 16 − 2·3·4·(1/2) = 13, so
a = √13.

**Example 7.** Optimization via derivative: minimize f(x) = x + 4/x for x > 0.
f′(x) = 1 − 4/x² = 0 → x = 2, f(2) = 4. (AM–GM gives the same: x + 4/x ≥
2√4 = 4.)

## Practice

1. An arithmetic sequence has a₃ = 7 and a₇ = 19. Find a₁, d and S₁₀.
   *(Answer: d = 3, a₁ = 1, S₁₀ = 145.)*
2. Sum the series 1/2 + 1/4 + 1/8 + … + 1/2¹⁰. *(Answer: 1 − 2⁻¹⁰ = 1023/1024.)*
3. Solve x² − 5x + 6 < 0. *(Answer: 2 < x < 3.)*
4. For x, y > 0 with x + y = 10, maximize xy. *(Answer: 25 at x = y = 5, by
   AM–GM.)*
5. Compute (1 + i)(2 − i) and |3 + 4i|. *(Answer: 3 + i; 5.)*
6. Find the monotonicity intervals and extrema of f(x) = x³ − 3x.
   *(Answer: increasing on (−∞,−1), (1,∞); local max f(−1) = 2, local min
   f(1) = −2.)*
7. Compute Σₖ₌₁ⁿ k² using the identity k² = k(k+1) − k and known sums.
   *(Answer: n(n+1)(2n+1)/6.)*
8. (Challenge) A recurrence aₙ₊₁ = 2aₙ + 1 with a₁ = 1. Find a closed form.
   *(Hint: add 1 to both sides → geometric. Answer: aₙ = 2ⁿ − 1.)*
