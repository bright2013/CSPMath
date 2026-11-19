# Elementary Matrix Transformations 【6】

矩阵的初等变换

## Description

The **elementary row transformations (初等行变换)** of a matrix are:

1. **Swap** two rows: Rᵢ ↔ Rⱼ;
2. **Scale** a row by a non-zero constant: Rᵢ ← c·Rᵢ (c ≠ 0);
3. **Add a multiple of one row to another**: Rᵢ ← Rᵢ + c·Rⱼ.

There are analogous **column transformations**. Elementary transformations are
the engine of [Gaussian elimination](gaussian-elimination.md).

**Why these three?** Because each corresponds to a legitimate manipulation of a
linear system: swapping two equations changes nothing; multiplying an equation
by c ≠ 0 keeps it equivalent; adding a multiple of one equation to another
preserves every solution (and creates none). In short: **row transformations
never change the solution set** of A·x = b when applied to the augmented matrix
(A|b).

**Key properties:**

* They are **reversible** — each has an inverse of the same type (swap undoes
  itself; scaling by c is undone by 1/c; adding c·Rⱼ is undone by adding
  −c·Rⱼ).
* They preserve the solution set of the linear system.
* They preserve the **rank** of the matrix — the true count of independent
  equations.
* Each row transformation equals left-multiplication by an **elementary
  matrix** (the identity matrix with the same operation applied). So a whole
  elimination is secretly one big matrix product Eₖ…E₂E₁·A.

A matrix reduced by row transformations to a form where each row's leading
non-zero entry (**pivot (主元)**) sits strictly right of the row above is in
**row echelon form (行阶梯形)**; with pivots = 1 and zeros above each pivot,
**reduced row echelon form (行最简形)**.

## Examples

**Example 1.** Swap R₁ ↔ R₂ on [[1, 2], [3, 4]] → [[3, 4], [1, 2]].

**Example 2.** Reduce A = [[2, 4], [1, 3]] to row echelon form:

```
R₁ ← R₁/2:   [1  2]
             [1  3]
R₂ ← R₂−R₁:  [1  2]
             [0  1]   ← row echelon form
```

**Example 3.** Continue to reduced form: R₁ ← R₁ − 2R₂ → [[1, 0], [0, 1]] = I.
The matrix was invertible; elimination revealed it.

**Example 4.** The elementary matrix for R₂ ← R₂ + 3R₁ (size 3) is
[[1,0,0],[3,1,0],[0,0,1]]; multiplying A by it on the left performs the row
operation.

**Example 5.** Computing A⁻¹ by transformations: row-reduce the double-wide
matrix (A | I) to (I | B); the same operations that turn A into I turn I into
B = A⁻¹. This is the standard hand-computation method and the proof that
"invertible ⇔ reduces to I".

## Practice

1. Starting from [[1, 2], [3, 7]], use one row-addition to zero the (2,1)
   entry. *(Answer: R₂ ← R₂ − 3R₁ → [[1,2],[0,1]].)*
2. Write the 3×3 elementary matrix performing R₃ ← R₃ − 2R₁.
   *(Answer: [[1,0,0],[0,1,0],[−2,0,1]].)*
3. Reduce [[1, 1, 2], [2, 3, 5], [1, 2, 3]] to row echelon form.
   *(Answer: R₂−2R₁, R₃−R₁ → rows [1,1,2], [0,1,0], [0,1,1]; then R₃−R₂ →
   [0,0,1]. Final: [[1,1,2],[0,1,0],[0,0,1]].)*
4. What is the inverse of the transformation Rᵢ ← c·Rᵢ? *(Answer: Rᵢ ← Rᵢ/c.)*
5. Show that if two rows of A are identical, one row-addition produces a zero
   row — hence rank < n and (for square A) det A = 0.
6. Reduce (A | I) for A = [[1, 2], [3, 4]] to find A⁻¹.
   *(Answer: [[−2, 1], [3/2, −1/2]].)*
7. (Challenge) Show that swap can be expressed using only scale and add
   operations. *(Hint: Rᵢ ← Rᵢ+Rⱼ, Rⱼ ← Rᵢ−Rⱼ, Rᵢ ← Rᵢ−Rⱼ gives a swap with a
   sign flip — finish with a scale by −1.)*
