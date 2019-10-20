# itertools.combinations_with_replacement()

https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

### Problem

itertools.combinations_with_replacement(iterable[, r])     

This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.  

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

**Task** 

You are given a string S.   

Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

**Input Format**

A single line containing the string S and integer value k separated by a space.

**Output Format**

Print the combinations with their replacements of string S on separate lines.

**Sample Input 0**

```
HACK 2
```

**Sample Output 0**

```
A
C
H
K
AC
AH
AK
CH
CK
HK
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)