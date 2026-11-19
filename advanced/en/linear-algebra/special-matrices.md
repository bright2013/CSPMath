# Special Matrices 【6】

特殊矩阵的概念：单位阵、三角阵、对称阵和稀疏矩阵

## Description

* **Identity matrix (单位阵)** I: square, aᵢᵢ = 1, all other entries 0. It is the
  multiplicative unit: A·I = I·A = A. Analogous to the number 1.
* **Triangular matrix (三角阵)**: **upper triangular** has aᵢⱼ = 0 for i > j (all
  zeros below the diagonal); **lower triangular** has zeros above. Products and
  inverses of triangular matrices stay triangular; the determinant is the product
  of the diagonal.
* **Symmetric matrix (对称阵)**: Aᵀ = A, i.e. aᵢⱼ = aⱼᵢ. Only n(n+1)/2 entries need
  storing. Graph adjacency matrices of undirected graphs are symmetric.
* **Sparse matrix (稀疏矩阵)**: most entries are zero. Store only the non-zeros:
  triples (row, col, value) — the **coordinate list (COO)** — or adjacency lists.
  An n-vertex graph with m edges: adjacency matrix takes O(n²) memory, adjacency
  lists O(n + m); for sparse graphs m ≪ n² the lists win decisively.

## Examples

**Example 1.** I₃ = [[1,0,0],[0,1,0],[0,0,1]]; check [[1,2],[3,4]]·I₂ =
[[1,2],[3,4]].

**Example 2.** Upper triangular: [[2, 5, 1], [0, 3, 4], [0, 0, 7]] — determinant
1·3·7 = 21 (product of the diagonal).

**Example 3.** Symmetric: [[1, 7, 3], [7, 2, 5], [3, 5, 0]]. The adjacency matrix
of an undirected graph is always symmetric: edge i–j appears at both (i, j) and
(j, i).

**Example 4 (C++).** Sparse storage as triples and as adjacency lists:

```cpp
struct Entry { int r, c; double v; };      // COO triple
vector<Entry> sparse = {{0, 1, 2.5}, {3, 3, -1.0}};

vector<vector<pair<int,int>>> g(n);        // adjacency list: (neighbor, weight)
g[u].push_back({v, w});
```

**Example 5.** The matrices appearing in Gaussian elimination end up upper
triangular — that is exactly the point of elimination: back-substitution on a
triangular system costs only O(n²).

## Practice

1. Which of these are symmetric/triangular? [[1,2],[2,3]]; [[1,2],[0,3]];
   [[1,0],[0,1]]. *(Answer: symmetric; upper triangular; both (and identity).)*
2. Is the product of two upper triangular 3×3 matrices upper triangular? Multiply
   two small examples and conjecture. *(Answer: yes.)*
3. A graph has 10⁵ vertices and 3×10⁵ edges. Adjacency matrix vs adjacency list —
   how much memory does each need (4-byte entries)? *(Answer: ≈ 4×10¹⁰ bytes vs
   ≈ 2×3×10⁵×8 ≈ 4.8 MB.)*
4. How many entries must be stored for a symmetric n×n matrix? For n = 1000 vs the
   full 10⁶? *(Answer: n(n+1)/2 = 500 500.)*
5. Write a program that reads a sparse matrix as (r, c, v) triples and computes
   A·x for a dense vector x without ever building the full matrix.
6. (Challenge) Show that a matrix that is both upper and lower triangular is
   diagonal, and that diagonal matrices commute with each other.
