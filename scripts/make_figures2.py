"""Generate a second wave of figures for the advanced-level GitBook spaces."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
import os

OUT = "assets-gen2"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"figure.dpi": 150, "font.size": 11, "axes.axisbelow": True})

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("made", name)

# ------------------------------------------------------------ 1. lattice path
fig, ax = plt.subplots(figsize=(5.4, 4.0))
W, H = 4, 3
for i in range(W + 1):
    ax.plot([i, i], [0, H], color="#d1d5db", lw=0.8)
for j in range(H + 1):
    ax.plot([0, W], [j, j], color="#d1d5db", lw=0.8)
path = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3)]
xs, ys = zip(*path)
ax.plot(xs, ys, color="#dc2626", lw=2.5, marker="o", ms=4)
steps = ["R", "U", "U", "R", "R", "U", "R"]
for (x0, y0), (x1, y1), s in zip(path, path[1:], steps):
    ax.text((x0 + x1) / 2 + 0.13, (y0 + y1) / 2 + 0.13, s, fontsize=10,
            color="#dc2626", weight="bold")
ax.text(-0.12, -0.25, "(0,0)", fontsize=10)
ax.text(4.0, 3.25, "(4,3)", fontsize=10)
ax.text(2, -0.7, "one path = one arrangement of {R×4, U×3}  →  C(7, 3) = 35",
        ha="center", fontsize=10)
ax.set_xlim(-0.5, 4.5); ax.set_ylim(-1.0, 3.6); ax.set_aspect("equal")
ax.axis("off")
save(fig, "lattice-path")

# --------------------------------------------------------- 2. multiset freq
fig, ax = plt.subplots(figsize=(5.0, 2.6))
letters = ["M", "I", "S", "P"]
counts = [1, 4, 4, 2]
bars = ax.bar(letters, counts, color=["#93c5fd", "#86efac", "#fde68a", "#fca5a5"],
              edgecolor="k")
for b, c in zip(bars, counts):
    ax.text(b.get_x() + b.get_width() / 2, c + 0.08, f"×{c}", ha="center",
            fontsize=11)
ax.set_title("MISSISSIPPI = {M×1, I×4, S×4, P×2},  |M| = 11", fontsize=10)
ax.set_ylim(0, 4.9); ax.spines[["top", "right"]].set_visible(False)
save(fig, "multiset-freq")

# ------------------------------------------------------------- 3. fast power
fig, ax = plt.subplots(figsize=(7.2, 2.4))
nodes = ["3¹", "3²", "3⁴", "3⁸"]
for i, t in enumerate(nodes):
    ax.add_patch(mp.FancyBboxPatch((i * 2.2, 0.9), 1.0, 0.62,
                                   boxstyle="round,pad=0.05", fc="#dbeafe",
                                   ec="k"))
    ax.text(i * 2.2 + 0.5, 1.21, t, ha="center", va="center", fontsize=12)
    if i < 3:
        ax.annotate("", xy=((i + 1) * 2.2 - 0.1, 1.21), xytext=(i * 2.2 + 1.1, 1.21),
                    arrowprops=dict(arrowstyle="->", lw=1.6))
        ax.text(i * 2.2 + 1.65, 1.5, "square", ha="center", fontsize=9)
ax.text(3.3, 0.3, "13 = 1101₂  →  3¹³ = 3⁸ · 3⁴ · 3¹   (bits that are 1)",
        ha="center", fontsize=11)
for i in [0, 2, 3]:
    ax.plot([i * 2.2 + 0.5], [0.62], marker="^", ms=9, color="#16a34a")
ax.text(4.4, -0.15, "green = multiplied into the result", ha="center",
        fontsize=9, color="#16a34a")
ax.set_xlim(-0.4, 7.4); ax.set_ylim(-0.4, 2.0); ax.set_aspect("equal")
ax.axis("off")
save(fig, "fast-power")

# ------------------------------------------------------------ 4. power cycle
fig, ax = plt.subplots(figsize=(4.6, 2.6))
vals = [pow(2, k, 7) for k in range(10)]
ax.plot(range(10), vals, "o-", color="#2563eb")
for k, v in enumerate(vals):
    ax.text(k, v + 0.16, str(v), ha="center", fontsize=9)
ax.axvspan(-0.4, 2.5, color="#fde68a", alpha=0.4)
ax.text(1, 5.9, "period 3: 1, 2, 4 repeats", fontsize=10, ha="center")
ax.set_xlabel("k"); ax.set_ylabel("2^k mod 7")
ax.set_xticks(range(10)); ax.set_ylim(0, 6.6)
ax.spines[["top", "right"]].set_visible(False)
save(fig, "power-cycle")

# -------------------------------------------------------------- 5. bezout line
fig, ax = plt.subplots(figsize=(7.0, 1.8))
ax.axhline(0, color="k", lw=1)
for x in range(-1, 13):
    v = 6 * x
    ax.plot([v, v], [-0.1, 0.1], color="#2563eb", lw=2)
    ax.text(v, 0.22, str(v), ha="center", fontsize=9, color="#2563eb")
ax.text(30, 0.85, "all values of 12x + 18y = multiples of gcd(12, 18) = 6",
        fontsize=10, ha="center")
ax.text(30, -0.75, "… and 6 itself = 12·(−1) + 18·1", fontsize=10, ha="center",
        color="#dc2626")
ax.plot([6], [0], "o", ms=9, mfc="none", mec="#dc2626", mew=2)
ax.set_xlim(-8, 76); ax.set_ylim(-1.1, 1.2)
ax.axis("off")
save(fig, "bezout-line")

# ----------------------------------------------------------- 6. inverse table
fig, ax = plt.subplots(figsize=(4.6, 4.2))
inv = {1: 1, 2: 4, 3: 5, 4: 2, 5: 3, 6: 6}
for a in range(1, 7):
    for b in range(1, 7):
        v = a * b % 7
        fc = "#86efac" if v == 1 else ("#f8fafc" if a <= b else "white")
        ax.add_patch(mp.Rectangle((b, 7 - a), 0.96, 0.96, fc=fc, ec="k", lw=0.5))
        ax.text(b + 0.48, 7 - a + 0.48, str(v), ha="center", va="center",
                fontsize=10)
for i in range(1, 7):
    ax.text(0.5, 7 - i + 0.48, str(i), ha="center", va="center", fontsize=11,
            weight="bold")
    ax.text(i + 0.48, 7.5, str(i), ha="center", va="center", fontsize=11,
            weight="bold")
ax.text(3.5, -0.15, "multiplication mod 7: a·b ≡ 1 (green) ⇔ b = a⁻¹",
        ha="center", fontsize=10)
ax.set_xlim(0, 7.2); ax.set_ylim(-0.5, 8.0); ax.set_aspect("equal")
ax.axis("off")
save(fig, "inverse-table")

# ----------------------------------------------------- 7. derangement letters
fig, ax = plt.subplots(figsize=(6.2, 2.8))
for i in range(4):
    ax.add_patch(mp.Rectangle((i * 1.7, 1.8), 1.1, 0.75, fc="#fde68a", ec="k"))
    ax.text(i * 1.7 + 0.55, 2.18, f"letter {i+1}", ha="center", fontsize=9)
    ax.add_patch(mp.Rectangle((i * 1.7, 0.2), 1.1, 0.75, fc="#dbeafe", ec="k"))
    ax.text(i * 1.7 + 0.55, 0.58, f"env. {i+1}", ha="center", fontsize=9)
mapping = [1, 0, 3, 2]  # a derangement: 2 1 4 3
for i, j in enumerate(mapping):
    ax.annotate("", xy=(j * 1.7 + 0.55, 1.05), xytext=(i * 1.7 + 0.55, 1.7),
                arrowprops=dict(arrowstyle="->", color="#16a34a", lw=1.8,
                                connectionstyle="arc3,rad=0.18"))
ax.text(2.9, 2.95, "a derangement of 4: (2, 1, 4, 3) — nobody gets their own",
        ha="center", fontsize=10)
ax.set_xlim(-0.4, 6.4); ax.set_ylim(-0.1, 3.3); ax.set_aspect("equal")
ax.axis("off")
save(fig, "derangement-letters")

# ------------------------------------------------------------ 8. catalan trees
fig, ax = plt.subplots(figsize=(7.4, 2.6))
shapes = [
    [(0, 0), (-1, -1), (-2, -2)],
    [(0, 0), (-1, -1), (-1.6, -2)],
    [(0, 0), (-1, -1), (1, -1)],
    [(0, 0), (1, -1), (1.6, -2)],
    [(0, 0), (1, -1), (2, -2)],
]
for k, tree in enumerate(shapes):
    ox = k * 6
    (r, c1, c2) = tree
    for p, q in [(r, c1), (c1, c2) if len(set([tuple(c1)])) else (r, c1)]:
        pass
    edges = [(0, 1), (1, 2)] if k != 2 else [(0, 1), (0, 2)]
    for e0, e1 in edges:
        p, q = tree[e0], tree[e1]
        ax.plot([ox + p[0], ox + q[0]], [p[1], q[1]], color="#6b7280", lw=1.4)
    for p in tree:
        ax.add_patch(mp.Circle((ox + p[0], p[1]), 0.18, fc="#93c5fd", ec="k"))
ax.text(12, 0.85, "the C₃ = 5 binary trees with 3 nodes", ha="center",
        fontsize=11)
ax.set_xlim(-3, 27); ax.set_ylim(-2.8, 1.2); ax.set_aspect("equal")
ax.axis("off")
save(fig, "catalan-trees")

# ------------------------------------------------------------------- 9. AM-GM
fig, ax = plt.subplots(figsize=(5.6, 3.0))
a, b = 2.0, 4.5
ax.plot([-a, b], [0, 0], "k", lw=2)
ax.text(-a / 2, -0.28, "a", ha="center", fontsize=12)
ax.text(b / 2, -0.28, "b", ha="center", fontsize=12)
R = (a + b) / 2
cx = (b - a) / 2
th = np.linspace(0, np.pi, 200)
ax.plot(cx + R * np.cos(th), R * np.sin(th), color="#2563eb", lw=1.6)
ax.plot([0, 0], [0, np.sqrt(a * b)], color="#dc2626", lw=2.5)
ax.text(0.08, np.sqrt(a * b) / 2, "√(ab)", color="#dc2626", fontsize=12)
ax.plot([cx, 0], [0, np.sqrt(a * b)], "--", color="#2563eb", lw=1.2)
ax.text(cx + 0.25, np.sqrt(a * b) * 0.72, "(a+b)/2", color="#2563eb",
        fontsize=12)
ax.text(cx, -0.7, "radius (a+b)/2 ≥ height √(ab) — equality iff a = b",
        ha="center", fontsize=10)
ax.set_xlim(-2.8, 5.3); ax.set_ylim(-1.1, 4.2); ax.set_aspect("equal")
ax.axis("off")
save(fig, "am-gm")

# ------------------------------------------------------------------ 10. conics
fig, axes = plt.subplots(1, 3, figsize=(8.4, 2.9))
t = np.linspace(0, 2 * np.pi, 300)
axes[0].plot(2 * np.cos(t), 1.2 * np.sin(t), "k")
axes[0].set_title("ellipse\nx²/a² + y²/b² = 1", fontsize=9)
u = np.linspace(-1.9, 1.9, 200)
for s in (1, -1):
    axes[1].plot(s * np.cosh(u) * 0.8, np.sinh(u) * 0.8, "k")
axes[1].set_title("hyperbola\nx²/a² − y²/b² = 1", fontsize=9)
v = np.linspace(-1.7, 1.7, 200)
axes[2].plot(v**2 / 2, v, "k")
axes[2].set_title("parabola\ny² = 2px", fontsize=9)
for ax_ in axes:
    ax_.axhline(0, color="#e5e7eb", lw=0.8); ax_.axvline(0, color="#e5e7eb", lw=0.8)
    ax_.set_aspect("equal"); ax_.set_xticks([]); ax_.set_yticks([])
    ax_.set_xlim(-2.4, 2.4); ax_.set_ylim(-2.2, 2.2)
fig.tight_layout()
save(fig, "conics")

# -------------------------------------------------------- 11. matrix transform
fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.0))
sq = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]])
M = np.array([[2.0, 1.0], [0.0, 1.0]])
for ax_, data, title in [(axes[0], sq, "before: unit square"),
                         (axes[1], M @ sq, "after: A · x, A = [[2,1],[0,1]]")]:
    ax_.fill(data[0], data[1], fc="#bfdbfe", ec="k", alpha=0.8)
    ax_.arrow(0, 0, *(data[:, 1] * 0.9), head_width=0.07, fc="#dc2626",
              ec="#dc2626")
    ax_.arrow(0, 0, *(data[:, 3] * 0.9), head_width=0.07, fc="#2563eb",
              ec="#2563eb")
    ax_.set_title(title, fontsize=9)
    ax_.set_aspect("equal"); ax_.set_xticks([]); ax_.set_yticks([])
    ax_.axhline(0, color="#e5e7eb", lw=0.8); ax_.axvline(0, color="#e5e7eb", lw=0.8)
axes[1].set_xlim(-0.5, 3.6); axes[1].set_ylim(-0.5, 2.2)
axes[0].set_xlim(-0.5, 1.8); axes[0].set_ylim(-0.5, 1.8)
fig.tight_layout()
save(fig, "matrix-transform")

# ----------------------------------------------------------------- 12. echelon
fig, ax = plt.subplots(figsize=(6.8, 2.4))
cell = 0.52
pivots = {(0, 0), (1, 1), (2, 3)}
for i in range(3):
    for j in range(5):
        if (i, j) in pivots:
            fc, t = "#86efac", "p"
        elif j < [c for (r, c) in pivots if r == i][0]:
            fc, t = "white", "0"
        else:
            fc, t = "#e5e7eb", "*"
        ax.add_patch(mp.Rectangle((j * cell, 3 * cell - i * cell), cell * 0.94,
                                  cell * 0.94, fc=fc, ec="k", lw=0.5))
        ax.text(j * cell + 0.48 * cell, 3 * cell - i * cell + 0.47 * cell, t,
                ha="center", va="center", fontsize=9)
ax.text(4 * cell, -0.35, "row echelon form: each pivot (green) strictly right of the one above,\nzeros below every pivot",
        ha="center", va="top", fontsize=9)
ax.set_xlim(-0.1, 3.1); ax.set_ylim(-1.3, 2.2); ax.set_aspect("equal")
ax.axis("off")
save(fig, "echelon")

# ------------------------------------------------------------ 13. sparse matrix
fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))
nz = [(0, 1), (0, 4), (2, 2), (3, 0), (4, 3)]
for i in range(5):
    for j in range(5):
        fc = "#fca5a5" if (i, j) in nz else "white"
        axes[0].add_patch(mp.Rectangle((j, 4 - i), 0.96, 0.96, fc=fc, ec="k",
                                       lw=0.4))
axes[0].set_title("5×5 matrix, only 5 nonzeros", fontsize=9)
axes[0].set_xlim(-0.1, 5.1); axes[0].set_ylim(-0.1, 5.1)
axes[0].set_aspect("equal"); axes[0].axis("off")
for k, (i, j) in enumerate(nz):
    axes[1].text(0, 4 - k, f"({i}, {j}, v{k+1})", fontsize=11, family="monospace")
axes[1].set_title("store only the triples (row, col, value)", fontsize=9)
axes[1].set_xlim(-0.2, 3.6); axes[1].set_ylim(-0.5, 4.8); axes[1].axis("off")
fig.tight_layout()
save(fig, "sparse-matrix")

# ----------------------------------------------------------------- 14. shoelace
fig, ax = plt.subplots(figsize=(4.6, 3.6))
poly = [(1, 1), (4, 1), (5, 3), (2, 4)]
xs = [p[0] for p in poly] + [poly[0][0]]
ys = [p[1] for p in poly] + [poly[0][1]]
ax.fill(xs, ys, fc="#dbeafe", ec="k", alpha=0.8)
for i, (x, y) in enumerate(poly):
    ax.plot(x, y, "o", color="#dc2626", ms=6)
    ax.text(x + 0.1, y + 0.14, f"p{i+1}({x},{y})", fontsize=9)
ax.text(3, 2.2, "2·Area = |Σ xᵢyᵢ₊₁ − Σ yᵢxᵢ₊₁|", ha="center", fontsize=10)
ax.set_xlim(0, 6); ax.set_ylim(0, 5); ax.set_aspect("equal")
ax.grid(color="#e5e7eb"); ax.set_xticks(range(7)); ax.set_yticks(range(6))
save(fig, "shoelace")

# --------------------------------------------------------------- 15. sierpinski
fig, ax = plt.subplots(figsize=(5.4, 4.6))
rows = 32
from math import comb
for n in range(rows):
    for k in range(n + 1):
        if comb(n, k) % 2 == 1:
            ax.add_patch(mp.Rectangle((k - n / 2, rows - n), 0.92, 0.92,
                                      fc="#2563eb", ec="none"))
ax.text(0, rows + 2.2, "odd entries of Pascal's triangle (32 rows)",
        ha="center", fontsize=10)
ax.set_xlim(-rows / 2 - 1, rows / 2 + 1); ax.set_ylim(0, rows + 3)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "pascal-odd")

# ----------------------------------------------------------------- 16. phi chart
fig, ax = plt.subplots(figsize=(5.6, 2.8))
ns = list(range(1, 13))
def phi(n):
    return sum(1 for a in range(1, n + 1) if np.gcd(a, n) == 1)
vals = [phi(n) for n in ns]
bars = ax.bar(ns, vals, color="#93c5fd", edgecolor="k")
bars[11].set_color("#fca5a5")
ax.text(12, vals[11] + 0.15, "φ(12)=4", ha="center", fontsize=10)
ax.text(12, vals[11] + 0.85, "1, 5, 7, 11", ha="center", fontsize=8)
ax.set_xticks(ns); ax.set_ylim(0, 5.2)
ax.set_title("φ(n) for n = 1…12", fontsize=10)
ax.spines[["top", "right"]].set_visible(False)
save(fig, "phi-chart")

print("all second-wave figures done")
