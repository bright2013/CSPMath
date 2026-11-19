# Vector Operations 【6】

向量的运算

## Description

For vectors a = (a₁, …, aₙ), b = (b₁, …, bₙ) and a scalar λ:

* **Addition/subtraction (加减)**: componentwise, (a ± b)ᵢ = aᵢ ± bᵢ.
* **Scalar multiplication (数乘)**: (λa)ᵢ = λ·aᵢ.
* **Dot product (数量积/点积)**: a·b = Σ aᵢbᵢ = |a||b|cos θ.
* **Norm (模)**: |a| = √(a·a) = √(Σ aᵢ²).
* **Cross product (叉积, 3D/planar)**: for 2D vectors the scalar cross product
  a × b = a₁b₂ − a₂b₁ gives the signed area of the parallelogram they span; its
  sign tells the turn direction (counterclockwise if positive).

**Key relations:**

* a ⊥ b ⇔ a·b = 0.
* cos θ = a·b / (|a||b|).
* a ∥ b ⇔ a × b = 0 (2D).

**In computational geometry**, dot and cross products are the atoms: orientation
tests, polygon area (½ Σ pᵢ × pᵢ₊₁), point-to-line distance, convex hulls.

## Examples

**Example 1.** a = (1, 2, 3), b = (4, 0, −1): a + b = (5, 2, 2),
a·b = 4 + 0 − 3 = 1, |a| = √14.

**Example 2.** Perpendicularity: (3, 4)·(−4, 3) = −12 + 12 = 0 → perpendicular.

**Example 3.** Signed area of triangle with vertices (0,0), (4,0), (1,3):
½ |(4, 0) × (1, 3)| = ½ |4·3 − 0·1| = 6.

**Example 4.** Orientation: is (0,0) → (2,1) → (1,3) a left turn?
(2,1) × ((1,3)−(2,1)) = (2,1) × (−1,2) = 2·2 − 1·(−1) = 5 > 0 → counterclockwise.

**Example 5 (C++).** The geometry toolkit:

```cpp
double dot(double x1, double y1, double x2, double y2) {
    return x1 * x2 + y1 * y2;
}
double cross(double x1, double y1, double x2, double y2) {
    return x1 * y2 - y1 * x2;
}
```

## Practice

1. a = (2, −1, 3), b = (1, 4, 0). Compute a + b, 3a − 2b, a·b, |a|, |b|.
   *(Answer: (3, 3, 3); (4, −11, 9); −2; √14; √17.)*
2. Find the angle between (1, 1) and (0, 1). *(Answer: cos θ = 1/√2 → 45°.)*
3. Find λ such that (λ, 2) ⊥ (3, −1). *(Answer: 3λ − 2 = 0 → λ = 2/3.)*
4. Area of the parallelogram spanned by (3, 1) and (2, 5). *(Answer: |2·5 − 1·2| =
   13.)*
5. Area of the polygon (0,0), (2,0), (2,2), (0,2) by the shoelace formula.
   *(Answer: 4.)*
6. Points A(0,0), B(3,0), C(2,2): is C to the left of the directed line AB?
   *(Answer: (3,0) × (2,2) = 6 > 0 → yes.)*
7. Write a program that reads a convex polygon's n vertices in order and prints its
   area using the shoelace formula ½ |Σ (xᵢyᵢ₊₁ − xᵢ₊₁yᵢ)|.
8. (Challenge) Prove a·b = |a||b|cos θ implies the Cauchy–Schwarz inequality
   |a·b| ≤ |a||b|.
