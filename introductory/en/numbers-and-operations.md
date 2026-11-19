# Numbers and Their Operations (数及其运算)

## Syllabus items

* 【1】Natural numbers, integers, rational numbers, real numbers and their
  arithmetic operations (addition, subtraction, multiplication, division)
  (自然数、整数、有理数、实数及其算术运算：加、减、乘、除)
* 【1】Number bases and base conversion: binary, octal, decimal, hexadecimal
  (进制与进制转换：二进制、八进制、十进制、十六进制)

## Numbers and arithmetic

* **Natural numbers (自然数)**: 0, 1, 2, 3, … used for counting.
* **Integers (整数)**: natural numbers together with their negatives …, −2, −1, 0, 1, 2, …
* **Rational numbers (有理数)**: numbers expressible as a fraction p/q with integer p
  and non-zero integer q, e.g. 1/2, −3, 0.25.
* **Real numbers (实数)**: rational numbers together with irrational numbers such as
  √2 and π.

You must be fluent in the four arithmetic operations (+, −, ×, ÷) over all of these
number sets, including the rules for signs and the order of operations.

## Number bases and conversion

A **base (进制)** fixes how many digits are used and what each position is worth:

| Base | Name | Digits | Example |
| --- | --- | --- | --- |
| 2 | Binary (二进制) | 0–1 | 1011₂ |
| 8 | Octal (八进制) | 0–7 | 13₈ |
| 10 | Decimal (十进制) | 0–9 | 11 |
| 16 | Hexadecimal (十六进制) | 0–9, A–F | B₁₆ |

**To decimal**: multiply each digit by its positional weight and add:

> 1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 11

**From decimal**: repeatedly divide by the target base and collect the remainders in
reverse order:

> 11 ÷ 2 = 5 r 1; 5 ÷ 2 = 2 r 1; 2 ÷ 2 = 1 r 0; 1 ÷ 2 = 0 r 1 → 1011₂

**Between binary, octal and hexadecimal**: group binary digits in threes (octal) or
fours (hexadecimal):

> 1011₂ = 001 011₂ = 13₈ = 1011₂ = B₁₆
