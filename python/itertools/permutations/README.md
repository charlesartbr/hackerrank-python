# itertools.permutations()

https://www.hackerrank.com/challenges/itertools-permutations

### Problem

itertools.permutations(iterable[, r])  

This tool returns successive  length permutations of elements in an iterable.  

If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.  

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.   

**Task** 

You are given a string S.   

Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

**Input Format**

A single line containing the space separated string S and the integer value k.

**Output Format**

Print the permutations of the string S on separate lines.

**Sample Input 0**

```
HACK 2
```

**Sample Output 0**

```
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)