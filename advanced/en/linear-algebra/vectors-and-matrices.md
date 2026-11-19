# Vectors and Matrices: Concepts 【5】

向量与矩阵的概念

## Description

A **vector (向量)** is an ordered tuple of numbers — a point or a displacement.
Written as a column x = (x₁, x₂, …, xₙ)ᵀ or a row. The **dimension** is n.

A **matrix (矩阵)** is a rectangular array of numbers with m **rows** and n
**columns**, denoted A = (aᵢⱼ) where aᵢⱼ is the entry in row i, column j. An m × n
matrix with m = n is **square (方阵)**.

* A row vector is a 1×n matrix; a column vector is m×1.
* Two matrices are **equal** iff they have the same shape and all entries match.
* The **zero matrix** O has all entries 0.

**Geometric view**: an m×n matrix represents a linear map from n-dimensional space
to m-dimensional space; multiplying A·x applies that map to the vector x.

**In programming**, matrices are 2D arrays `double a[N][M]`; vectors are 1D arrays.
They power: linear recurrences (matrix exponentiation), Gaussian elimination,
graph adjacency matrices, and dynamic programming transitions.

## Examples

**Example 1.** A = [[1, 2, 3], [4, 5, 6]] is 2×3; a₂₁ = 4, a₁₃ = 3.

**Example 2.** v = (3, 4)ᵀ is a 2-d column vector; its length (norm) is √(3²+4²) = 5.

**Example 3.** The adjacency matrix of a triangle graph on {1,2,3}:
A = [[0,1,1],[1,0,1],[1,1,0]] — symmetric, with 0 diagonal.

**Example 4.** A 3×3 matrix storing rotations about the z-axis by angle θ:

```
[cos θ  −sin θ  0]
[sin θ   cos θ  0]
[  0       0    1]
```

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
   *(Answer: the number of 2-step walks from i to j.)*
5. Store the matrix [[1,2],[3,4]] in C++ and print its transpose by swapping
   indices.
6. (Challenge) Explain why a 2×2 matrix [[0, −1], [1, 0]] rotates every vector by
   90° counterclockwise — apply it to (1,0)ᵀ and (0,1)ᵀ.
