# Day 26: Nested Logic

https://www.hackerrank.com/challenges/30-nested-logic

### Problem

Today's challenge puts your understanding of nested conditional statements to the test. 

**Task**

Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, **fine = 15 Hackos x (the days of days late)**.
3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the **fine = 500 Hackos x (the days of months late)**.
4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of **10000 Hackos**.

**Input Format**

The first line contains 3 space-separated integers denoting the respective day, month, and year on which the book was actually returned.  
The second line contains 3 space-separated integers denoting the respective day, month, and year on which the book was expected to be returned (due date).

**Output Format**

Print a single integer denoting the library fine for the book received as input.

**Sample Input**

```
9 6 2015
6 6 2015
```

**Sample Output**

```
45
```

### My Solution

- [Python 3](python3.py)