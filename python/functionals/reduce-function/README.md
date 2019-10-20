# Reduce Function

https://www.hackerrank.com/challenges/reduce-function

### Problem

Given a list of rational numbers, find their product.

**Concept**  
The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.

**Input Format**

First line contains N, the number of rational numbers. 
The i<sup>th</sup> of next N lines contain two integers each, the numerator(N<sub>i</sub>) and denominator(D<sub>i</sub>) of the i<sup>th</sup> rational number in the list.

**Output Format**

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.

**Sample Input 0**

```
3
1 2
3 4
10 6
```

**Sample Output 0**

```
5 8
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)