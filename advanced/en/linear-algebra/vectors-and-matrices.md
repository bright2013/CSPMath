# Vectors and Matrices: Concepts 【5】

向量与矩阵的概念

## Description

A **vector (向量)** is an ordered tuple of numbers — a point, a displacement, or
a state. Written as a column x = (x₁, x₂, …, xₙ)ᵀ or a row. The **dimension** is
n.

A **matrix (矩阵)** is a rectangular array of numbers with m **rows** and n
**columns**, denoted A = (aᵢⱼ) where aᵢⱼ is the entry in row i, column j. An
m × n matrix with m = n is **square (方阵)**.

* A row vector is a 1×n matrix; a column vector is m×1. Vectors are degenerate
  matrices — everything said about matrices applies to them.
* Two matrices are **equal** iff they have the same shape and all entries match.
* The **zero matrix** O has all entries 0 — the additive identity.

**Geometric view — the one to internalize**: an m×n matrix is a *linear map*
from n-dimensional space to m-dimensional space; computing A·x applies that map
to the vector x. "Linear" means the map respects addition and scaling:
A(u + v) = Au + Av and A(λu) = λ·Au. Rotations, scalings, projections, and
shears are all matrices; and conversely, every matrix is a combination of such
simple deformations. Column j of A is exactly where the j-th basis vector lands
under the map — read a matrix column-by-column to *see* what it does.

![The matrix [[2,1],[0,1]] shears and stretches the unit square into a parallelogram](../.gitbook/assets/matrix-transform.png)

Watch the two basis arrows in the figure: the red arrow (1,0) lands at (2,0) —
that is column 1 of A; the blue arrow (0,1) lands at (1,1) — that is column 2.
The whole square comes along for the ride. *Every* linear map works this way:
decide where the basis vectors go, and every other point follows.

**In programming**, matrices are 2D arrays `double a[N][M]`; vectors are 1D
arrays. They power: linear recurrences (matrix exponentiation), Gaussian
elimination, graph adjacency matrices, and dynamic programming transitions.

## Examples

**Example 1.** A = [[1, 2, 3], [4, 5, 6]] is 2×3; a₂₁ = 4, a₁₃ = 3. (Index
convention: row first, column second — `a[i][j]` in code.)

**Example 2.** v = (3, 4)ᵀ is a 2-d column vector; its length (norm) is
√(3²+4²) = 5.

**Example 3.** The adjacency matrix of a triangle graph on {1,2,3}:
A = [[0,1,1],[1,0,1],[1,1,0]] — symmetric, with 0 diagonal.

**Example 4.** A 3×3 matrix rotating about the z-axis by angle θ:

```
[cos θ  −sin θ  0]
[sin θ   cos θ  0]
[  0       0    1]
```

Read it by columns: the x-axis maps to (cos θ, sin θ, 0), the y-axis to
(−sin θ, cos θ, 0), the z-axis stays put — exactly a rotation.

**Example 5 (C++).** Declarations:

```cpp
double A[10][10];        // 10×10 matrix
double v[10];            // 10-d vector
vector<vector<double>> B(n, vector<double>(m));   // dynamic n×m
```

## Practice

1. For A = [[2, −1], [0, 3], [5, 5]], give its shape and the entries a₁₂, a₃₁.
   *(Answer: 3×2; −1; 5.)*
2. Is [[1, 2]] a vector or a matrix? *(Answer: both — a 1×2 matrix, i.e. a row
   vector.)*
3. Write the 4×4 zero matrix and the 2×3 matrix with aᵢⱼ = i + j.
   *(Answer: [[2,3,4],[3,4,5]].)*
4. A graph has adjacency matrix A. What does the entry of A² at (i, j) count?
   *(Answer: the number of 2-step walks from i to j — see
   [matrix operations](matrix-operations.md).)*
5. What does the matrix [[2, 0], [0, 3]] do geometrically to the plane?
   *(Answer: stretches x-coordinates ×2 and y-coordinates ×3.)*
6. Store the matrix [[1,2],[3,4]] in C++ and print its transpose by swapping
   indices.
7. (Challenge) Explain why [[0, −1], [1, 0]] rotates every vector by 90°
   counterclockwise — apply it to (1,0)ᵀ and (0,1)ᵀ and read the columns.
