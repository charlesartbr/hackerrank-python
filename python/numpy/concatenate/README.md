# Concatenate

https://www.hackerrank.com/challenges/np-concatenate

**Problem**

Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined.

**Task**

You are given two integer arrays of size N X P and M X P (N & M are rows, and P is the column). 
Your task is to concatenate the arrays along axis 0.

**Input Format**
    
The first line contains space separated integers N, M and P. 
The next N lines contains the space separated elements of the P columns. 
After that, the next M lines contains the space separated elements of the P columns.

**Output Format**

Print the concatenated array of size (N + M) X P.

**Sample Input 0**

```
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
```

**Sample Output 0**

```
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)