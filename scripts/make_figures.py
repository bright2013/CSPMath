"""Generate figures for the advanced-level GitBook spaces."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
import os

OUT = "assets-gen"
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"figure.dpi": 150, "font.size": 11, "axes.axisbelow": True})

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("made", name)

# ---------------------------------------------------------------- 1. gcd tiling
fig, ax = plt.subplots(figsize=(7.2, 2.8))
# gcd(48, 18): 48 = 2*18 + 12; 18 = 1*12 + 6; 12 = 2*6
ax.add_patch(mp.Rectangle((0, 0), 18, 18, fc="#dbeafe", ec="k"))
ax.add_patch(mp.Rectangle((18, 0), 18, 18, fc="#dbeafe", ec="k"))
ax.add_patch(mp.Rectangle((36, 6), 12, 12, fc="#bbf7d0", ec="k"))
ax.add_patch(mp.Rectangle((36, 0), 6, 6, fc="#fde68a", ec="k"))
ax.add_patch(mp.Rectangle((42, 0), 6, 6, fc="#fde68a", ec="k"))
for x, y, t in [(9, 9, "18×18"), (27, 9, "18×18"), (42, 12, "12×12"),
                (39, 3, "6×6"), (45, 3, "6×6")]:
    ax.text(x, y, t, ha="center", va="center", fontsize=10)
ax.annotate("", xy=(48, -1.5), xytext=(0, -1.5), arrowprops=dict(arrowstyle="<->"))
ax.text(24, -3.2, "48", ha="center")
ax.annotate("", xy=(-1.5, 18), xytext=(-1.5, 0), arrowprops=dict(arrowstyle="<->"))
ax.text(-3.4, 9, "18", va="center")
ax.set_xlim(-6, 50); ax.set_ylim(-5, 20); ax.set_aspect("equal"); ax.axis("off")
save(fig, "gcd-rectangle")

# ---------------------------------------------------------- 2. Eratosthenes grid
fig, ax = plt.subplots(figsize=(7.5, 3.4))
N, cols = 30, 10
state = {n: "p" for n in range(2, N + 1)}  # p = prime candidate
for p in (2, 3, 5):
    for m in range(2 * p, N + 1, p):
        state[m] = {2: "x2", 3: "x3", 5: "x5"}[p] if state[m] == "p" else state[m] + "" 
# simpler: recompute marks by smallest sieving prime
mark = {}
for p in (2, 3, 5):
    for m in range(p * p, N + 1, p):
        mark.setdefault(m, p)
colors = {2: "#fecaca", 3: "#fde68a", 5: "#bfdbfe"}
for n in range(1, N + 1):
    r, c = divmod(n - 1, cols)
    x, y = c, 2 - r
    if n == 1:
        fc, tcol = "#e5e7eb", "#6b7280"
    elif n in mark:
        fc, tcol = colors[mark[n]], "#374151"
    else:
        fc, tcol = "#86efac", "black"
    ax.add_patch(mp.Rectangle((x, y), 0.94, 0.94, fc=fc, ec="k", lw=0.6))
    ax.text(x + 0.47, y + 0.47, str(n), ha="center", va="center", color=tcol,
            fontsize=9)
ax.text(0, 3.15, "primes", color="#16a34a", fontsize=9, weight="bold")
ax.text(2.2, 3.15, "×2", color="#b91c1c", fontsize=9, weight="bold")
ax.text(3.4, 3.15, "×3", color="#b45309", fontsize=9, weight="bold")
ax.text(4.6, 3.15, "×5", color="#1d4ed8", fontsize=9, weight="bold")
ax.set_xlim(-0.2, 10.2); ax.set_ylim(-0.3, 3.5); ax.set_aspect("equal")
ax.axis("off")
save(fig, "sieve-eratosthenes")

# ----------------------------------------------------------------- 3. Venn 3
fig, ax = plt.subplots(figsize=(4.6, 3.6))
for (x, y), c, lab in zip([(0, 0.25), (-0.9, -0.75), (0.9, -0.75)],
                          ["#93c5fd", "#fca5a5", "#86efac"], ["A", "B", "C"]):
    ax.add_patch(mp.Circle((x, y), 1.35, fc=c, ec="k", alpha=0.55))
    ax.text(x * 1.55 - 0.05, y * 1.55, lab, fontsize=14, weight="bold")
for pos, t in [((-0.95, 0.5), "|A|"), ((0.95, 0.45), "|B|"), ((0, -1.28), "|C|"),
               ((0, 0.05), "A∩B∩C"), ((-0.55, -0.42), "−|A∩C|"),
               ((0.55, -0.42), "−|B∩C|"), ((0, 0.72), "−|A∩B|")]:
    ax.text(*pos, t, ha="center", fontsize=9)
ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.4, 1.9); ax.set_aspect("equal")
ax.axis("off")
save(fig, "venn3")

# -------------------------------------------------------------- 4. stars & bars
fig, ax = plt.subplots(figsize=(7.0, 1.4))
items = ["star"] * 3 + ["bar"] + ["star"] * 5 + ["star"] * 0 + ["bar"] + ["star"] * 2
x = 0
for it in items:
    if it == "star":
        ax.add_patch(mp.Circle((x, 0), 0.32, fc="#fbbf24", ec="k"))
        ax.text(x, 0, "★", ha="center", va="center", fontsize=15)
    else:
        ax.plot([x, x], [-0.55, 0.55], color="k", lw=3)
    x += 1
ax.text(1, -1.15, "x₁ = 3", ha="center", fontsize=12)
ax.text(5.5, -1.15, "x₂ = 5", ha="center", fontsize=12)
ax.text(9, -1.15, "x₃ = 2", ha="center", fontsize=12)
ax.text(4.5, 0.95, "x₁ + x₂ + x₃ = 10  →  C(10+3−1, 3−1) = C(12, 2) = 66",
        ha="center", fontsize=11)
ax.set_xlim(-1, 10); ax.set_ylim(-1.6, 1.5); ax.set_aspect("equal"); ax.axis("off")
save(fig, "stars-bars")

# ----------------------------------------------------------------- 5. Dyck path
fig, ax = plt.subplots(figsize=(4.2, 4.2))
n = 4
for i in range(n + 1):
    ax.plot([i, i], [0, n], color="#d1d5db", lw=0.8)
    ax.plot([0, n], [i, i], color="#d1d5db", lw=0.8)
ax.plot([0, n], [0, n], ls="--", color="#9ca3af")
path = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4), (4, 4)]
xs, ys = zip(*path)
ax.plot(xs, ys, color="#dc2626", lw=2.5, marker="o", ms=4)
bad = [(0, 0), (0, 1), (1, 1), (1, 3), (3, 3), (3, 4), (4, 4)]
bx, by = zip(*bad)
ax.plot(bx, by, color="#2563eb", lw=1.6, marker="s", ms=3, alpha=0.8)
ax.text(4.05, 0.1, "R", fontsize=9); ax.text(-0.15, 4.05, "U", fontsize=9)
ax.set_xlim(-0.3, n + 0.3); ax.set_ylim(-0.3, n + 0.4); ax.set_aspect("equal")
ax.axis("off")
save(fig, "dyck-path")

# --------------------------------------------------------------- 6. vector ops
fig, ax = plt.subplots(figsize=(5.4, 3.6))
a = np.array([4.0, 1.0]); b = np.array([1.5, 2.5])
ax.arrow(0, 0, *a, head_width=0.12, fc="#2563eb", ec="#2563eb", lw=2)
ax.arrow(0, 0, *b, head_width=0.12, fc="#dc2626", ec="#dc2626", lw=2)
ax.arrow(*a, *b, head_width=0.12, fc="#dc2626", ec="#dc2626", lw=1, alpha=0.45,
         linestyle="--")
ax.arrow(0, 0, *(a + b), head_width=0.12, fc="#7c3aed", ec="#7c3aed", lw=2)
poly = plt.Polygon([(0, 0), a, a + b, b], fc="#ede9fe", alpha=0.5, ec="none")
ax.add_patch(poly)
ax.text(4.15, 0.85, "a", fontsize=13, color="#2563eb", weight="bold")
ax.text(1.35, 2.62, "b", fontsize=13, color="#dc2626", weight="bold")
ax.text(2.9, 2.1, "a + b", fontsize=13, color="#7c3aed", weight="bold")
theta = np.linspace(np.arctan2(a[1], a[0]), np.arctan2(b[1], b[0]), 30)
ax.plot(1.1 * np.cos(theta), 1.1 * np.sin(theta), "k", lw=1)
ax.text(1.45, 0.55, "θ", fontsize=12)
ax.text(3.3, 2.75, "a × b = a₁b₂ − a₂b₁  (signed area)", fontsize=10)
ax.set_xlim(-0.4, 6.2); ax.set_ylim(-0.4, 3.9); ax.set_aspect("equal")
ax.axis("off")
save(fig, "vector-ops")

# ------------------------------------------------------------------ 7. ellipse
fig, ax = plt.subplots(figsize=(5.6, 3.4))
aa, bb = 5, 3
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(5 * np.cos(t), 3 * np.sin(t), "k", lw=1.8)
c = np.sqrt(aa**2 - bb**2)
ax.plot([-c, c], [0, 0], "o", color="#dc2626", ms=6)
ax.text(-c, -0.55, "F₁(−c,0)", ha="center", fontsize=10, color="#dc2626")
ax.text(c, -0.55, "F₂(c,0)", ha="center", fontsize=10, color="#dc2626")
P = np.array([5 * np.cos(0.9), 3 * np.sin(0.9)])
ax.plot(*P, "o", color="#2563eb", ms=6)
ax.plot([-c, P[0]], [0, P[1]], "--", color="#6b7280")
ax.plot([c, P[0]], [0, P[1]], "--", color="#6b7280")
ax.text(P[0] + 0.15, P[1] + 0.15, "P", fontsize=12, color="#2563eb")
ax.text(0, -3.9, "x²/a² + y²/b² = 1,   |PF₁| + |PF₂| = 2a,   c² = a² − b²",
        ha="center", fontsize=10)
ax.axhline(0, color="#d1d5db", lw=0.8); ax.axvline(0, color="#d1d5db", lw=0.8)
ax.set_xlim(-6, 6); ax.set_ylim(-4.4, 3.6); ax.set_aspect("equal"); ax.axis("off")
save(fig, "ellipse")

# --------------------------------------------------------- 8. matrix multiply
fig, ax = plt.subplots(figsize=(7.0, 3.0))
cell = 0.55
def draw_mat(ox, oy, n, m, fc, label=None):
    for i in range(n):
        for j in range(m):
            ax.add_patch(mp.Rectangle((ox + j * cell, oy - i * cell), cell * 0.96,
                                      cell * 0.96, fc=fc, ec="k", lw=0.5))
# A 3x2 (left), B 2x4 (right), C 3x4 (far right)
draw_mat(0, 2 * cell, 3, 2, "#e5e7eb")
draw_mat(2.4, 3 * cell + 0.6, 2, 4, "#e5e7eb")
draw_mat(6.2, 2 * cell, 3, 4, "#e5e7eb")
# highlight row 1 of A, col 2 of B, cell (0,2) of C
for j in range(2):
    ax.add_patch(mp.Rectangle((j * cell, cell), cell * 0.96, cell * 0.96,
                              fc="#93c5fd", ec="k"))
for i in range(2):
    ax.add_patch(mp.Rectangle((2.4 + 2 * cell, 3 * cell + 0.6 - i * cell),
                              cell * 0.96, cell * 0.96, fc="#fca5a5", ec="k",
                              lw=0.5))
ax.add_patch(mp.Rectangle((6.2 + 2 * cell, 2 * cell), cell * 0.96, cell * 0.96,
                          fc="#86efac", ec="k", lw=0.8))
ax.text(-0.55, 1.5 * cell, "row i", rotation=90, va="center", fontsize=9)
ax.text(2.4 + 2.5 * cell, 3 * cell + 0.95, "col j", ha="center", fontsize=9)
ax.text(8.6, 1.5 * cell, "cᵢⱼ = Σ aᵢₜ bₜⱼ", fontsize=10, va="center")
ax.text(1.8, cell * 1.5, "×", fontsize=16)
ax.text(5.7, cell * 1.5, "=", fontsize=16)
ax.text(0.55, -0.35, "m×k", ha="center", fontsize=10)
ax.text(3.5, 0.9, "k×n", ha="center", fontsize=10)
ax.text(7.3, -0.35, "m×n", ha="center", fontsize=10)
ax.set_xlim(-0.7, 9.2); ax.set_ylim(-0.7, 3.2); ax.set_aspect("equal")
ax.axis("off")
save(fig, "matrix-mult")

# ---------------------------------------------------------- 9. Gaussian elim
fig, ax = plt.subplots(figsize=(7.4, 2.6))
cell = 0.5
def mat(ox, oy, fill_fn, n=3, m=4):
    for i in range(n):
        for j in range(m):
            fc = fill_fn(i, j)
            ax.add_patch(mp.Rectangle((ox + j * cell, oy - i * cell),
                                      cell * 0.94, cell * 0.94, fc=fc, ec="k",
                                      lw=0.5))
def f1(i, j):
    return "#dbeafe" if j == 3 else "#e5e7eb"
def f2(i, j):
    if j == 3: return "#dbeafe"
    if j < i or (j == i): return "#e5e7eb"
    return "#fde68a" if j > i and i > 0 else "#e5e7eb"
def f3(i, j):
    if j == 3: return "#dbeafe"
    if i == j: return "#86efac"
    if j < i: return "white"
    return "#e5e7eb"
mat(0, 2 * cell, f1); ax.text(1.0, -0.4, "(A | b)", ha="center", fontsize=10)
ax.text(2.35, 0.75 * cell, "→", fontsize=16)
mat(2.9, 2 * cell, f2); ax.text(3.9, -0.4, "eliminate below pivots", ha="center", fontsize=9)
ax.text(5.25, 0.75 * cell, "→", fontsize=16)
mat(5.8, 2 * cell, f3); ax.text(6.8, -0.4, "upper triangular → back-substitute", ha="center", fontsize=9)
ax.set_xlim(-0.2, 8.6); ax.set_ylim(-0.8, 1.8); ax.set_aspect("equal")
ax.axis("off")
save(fig, "gaussian-elim")

# --------------------------------------------------------- 10. CRT number line
fig, ax = plt.subplots(figsize=(7.4, 2.2))
xs = np.arange(0, 106)
m3 = xs[xs % 3 == 2]; m5 = xs[xs % 5 == 3]; m7 = xs[xs % 7 == 2]
ax.scatter(m3, [3] * len(m3), s=14, color="#2563eb")
ax.scatter(m5, [2] * len(m5), s=18, color="#dc2626")
ax.scatter(m7, [1] * len(m7), s=14, color="#16a34a")
for y, t in [(3, "mod 3 = 2"), (2, "mod 5 = 3"), (1, "mod 7 = 2")]:
    ax.text(-2, y, t, ha="right", va="center", fontsize=10)
for y in (1, 2, 3):
    ax.plot([23, 23], [y - 0.32, y + 0.32], color="k", lw=1.5)
ax.scatter([23], [3.6], marker="v", s=90, color="black")
ax.text(23, 3.85, "x = 23", ha="center", fontsize=12, weight="bold")
ax.set_xlim(-14, 106); ax.set_ylim(0.3, 4.3)
ax.axis("off")
save(fig, "crt-numberline")

# -------------------------------------------------------------- 11. pigeonhole
fig, ax = plt.subplots(figsize=(6.4, 2.2))
for i in range(4):
    ax.add_patch(mp.Rectangle((i * 1.5, 0), 1.2, 0.9, fc="#e5e7eb", ec="k"))
rng = np.random.default_rng(7)
for i, cnt in enumerate([2, 1, 3, 1]):
    for k in range(cnt):
        ax.add_patch(mp.Circle((i * 1.5 + 0.3 + 0.3 * (k % 2),
                                0.25 + 0.35 * (k // 2)), 0.11, fc="#f59e0b",
                               ec="k"))
ax.text(2.8, 1.25, "7 pigeons, 4 holes → some hole has ≥ ⌈7/4⌉ = 2",
        ha="center", fontsize=11)
ax.set_xlim(-0.3, 6.1); ax.set_ylim(-0.2, 1.6); ax.set_aspect("equal")
ax.axis("off")
save(fig, "pigeonhole")

# ------------------------------------------------------------- 12. round table
fig, ax = plt.subplots(figsize=(3.6, 3.6))
ax.add_patch(mp.Circle((0, 0), 0.62, fc="#fef3c7", ec="k"))
n = 6
for i in range(n):
    th = np.pi / 2 - i * 2 * np.pi / n
    x, y = 1.25 * np.cos(th), 1.25 * np.sin(th)
    ax.add_patch(mp.Circle((x, y), 0.21, fc="#93c5fd", ec="k"))
    ax.text(x, y, str(i + 1), ha="center", va="center", fontsize=10)
ax.text(0, 0, "(n−1)!", ha="center", va="center", fontsize=14, weight="bold")
ax.set_xlim(-1.8, 1.8); ax.set_ylim(-1.8, 1.8); ax.set_aspect("equal")
ax.axis("off")
save(fig, "round-table")

# --------------------------------------------------------- 13. modular clock
fig, ax = plt.subplots(figsize=(3.8, 3.8))
ax.add_patch(mp.Circle((0, 0), 1.0, fc="#f8fafc", ec="k"))
m = 7
for i in range(m):
    th = np.pi / 2 - i * 2 * np.pi / m
    x, y = 0.82 * np.cos(th), 0.82 * np.sin(th)
    ax.text(x, y, str(i), ha="center", va="center", fontsize=11)
ax.annotate("", xy=(0.82 * np.cos(np.pi / 2 - 3 * 2 * np.pi / m + 0.32),
                    0.82 * np.sin(np.pi / 2 - 3 * 2 * np.pi / m + 0.32)),
            xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color="#dc2626", lw=2))
ax.text(0, -0.28, "38 mod 7 = 3", ha="center", fontsize=11, color="#dc2626")
ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.25, 1.2); ax.set_aspect("equal")
ax.axis("off")
save(fig, "mod-clock")

print("all figures done")
