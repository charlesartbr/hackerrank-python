# itertools.product()

https://www.hackerrank.com/challenges/itertools-product

### Problem

itertools.product(iterable[, r])  

This tool computes the cartesian product of input iterables.   

It is equivalent to nested for-loops.   

For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

**Task** 

You are given a two lists A and B. Your task is to compute their cartesian product A X B.

**Input Format**

The first line contains the space separated elements of list A.   
The second line contains the space separated elements of list B.  

Both lists have no duplicate integer elements.

**Output Format**

Output the space separated tuples of the cartesian product.

**Sample Input 0**

```
 1 2
 3 4
```

**Sample Output 0**

```
 (1, 3) (1, 4) (2, 3) (2, 4)
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)