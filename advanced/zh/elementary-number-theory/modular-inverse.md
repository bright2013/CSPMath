# 模运算意义下的逆元 【7】

## 讲解

a 在模 m 意义下的**逆元**是满足下式的整数 x：

> a·x ≡ 1 (mod m)

记作 a⁻¹ (mod m)。**存在当且仅当 gcd(a, m) = 1**，存在时模 m 唯一。

有了逆元，模运算中的**除法**成为可能："除以 a"等于"乘以 a⁻¹"：

> b / a (mod m) ≡ b · a⁻¹ (mod m)

**三种求法：**

1. **扩展欧几里得算法**——任意模数 m 且 gcd(a, m) = 1 都适用：解
   a·x + m·y = 1，则 x ≡ a⁻¹ (mod m)。O(log m)。
2. **费马小定理**——模数为质数 p 时：a⁻¹ ≡ a^(p−2) (mod p)，快速幂求得。
   O(log p)。
3. **质数模下逆元的线性递推**：inv[i] = (p − p/i) · inv[p % i] % p，
   O(n) 预处理出 inv[1..n]。

**典型应用**：求 C(n, m) mod p——预处理阶乘与阶乘逆元，则
C(n,m) = fact[n] · invFact[m] · invFact[n−m] mod p。

## 例题

**例 1.** 3⁻¹ mod 7 = 5，因为 3·5 = 15 ≡ 1 (mod 7)。

**例 2.** 计算 1/2 + 1/3 (mod 7)：2⁻¹ = 4，3⁻¹ = 5 → 4 + 5 = 9 ≡ 2 (mod 7)。
验证：1/2 + 1/3 = 5/6，而 5·6⁻¹ = 5·6 = 30 ≡ 2（6 模 7 自逆）。✓

**例 3.** 6⁻¹ mod 9 不存在：gcd(6, 9) = 3 ≠ 1（6x ≡ 1 (mod 9) 要求 3 | 1）。

**例 4（C++）.** 质数模下用快速幂求逆元，以及 O(n) 逆元表：

```cpp
long long inv(long long a, long long p) { return qpow(a, p - 2, p); }

// 质数 p 下 1..n 的逆元，O(n)：
inv[1] = 1;
for (int i = 2; i <= n; i++)
    inv[i] = (p - p / i) * inv[p % i] % p;
```

**例 5（C++）.** 模 998244353 的组合数：

```cpp
fact[0] = 1;
for (int i = 1; i <= N; i++) fact[i] = fact[i-1] * i % P;
invFact[N] = qpow(fact[N], P - 2, P);
for (int i = N; i >= 1; i--) invFact[i-1] = invFact[i] * i % P;
// C(n, m) = fact[n] * invFact[m] % P * invFact[n-m] % P
```

## 练习

1. 手算：2⁻¹ mod 5；5⁻¹ mod 7；10⁻¹ mod 13；7⁻¹ mod 12。
   *（答案：3；3；4；7。）*
2. 哪些存在逆元：4 mod 9；6 mod 15；11 mod 26？*（答案：有；无；有。）*
3. 计算 5/3 mod 11（即 5·3⁻¹ mod 11）。*（答案：3⁻¹ = 4，故 20 ≡ 9。）*
4. 用费马小定理计算 2⁻¹ mod 1000000007。*（答案：500000004 = (p+1)/2。）*
5. 对 p = 7、i = 1…6 逐一验证递推 inv[i] = (p − p/i)·inv[p%i] % p，并与暴力
   结果对照。
6. 编写程序：模 998244353 下回答 q 组 C(n, m) 查询，n ≤ 10⁶。
7. （挑战）证明递推公式：写 p = q·i + r（r = p mod i），则 q·i + r ≡ 0 (mod p)，
   从而 i⁻¹ ≡ −q·r⁻¹ (mod p)。
