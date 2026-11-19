# Others: ASCII Code (其他：ASCII 码)

## Syllabus item

* 【2】ASCII code (ASCII 码)

## What ASCII is

**ASCII (American Standard Code for Information Interchange)** assigns a 7-bit code
(0–127) to each character. It is the basis of character representation in computers.

Key ranges to remember:

| Characters | Decimal codes |
| --- | --- |
| '0'–'9' | 48–57 |
| 'A'–'Z' | 65–90 |
| 'a'–'z' | 97–122 |
| Space | 32 |

Useful facts:

* Digits are contiguous: '5' − '0' = 5 converts a digit character to its value.
* Uppercase and lowercase differ by 32: 'a' − 'A' = 32.
* Codes 0–31 and 127 are control characters (e.g. newline is 10).

In C/C++, a `char` stores its ASCII code, so characters can take part directly in
arithmetic and comparisons.
