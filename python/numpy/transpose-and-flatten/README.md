# Transpose and Flatten

https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

**Problem**

**Transpose**
We can generate the transposition of an array using the tool numpy.transpose.   
It will not affect the original array, but it will create a new array.

**Flatten**
The tool flatten creates a copy of the input array flattened to one dimension.

**Task**

You are given a N X M integer array matrix with space separated elements (N = rows and M = columns).   
Your task is to print the transpose and flatten results.

**Input Format**
    
The first line contains the space separated values of N and M. 
The next N lines contains the space separated elements of M columns.

**Output Format**

First, print the transpose array and then print the flatten.

**Sample Input 0**

```
2 2
1 2
3 4
```

**Sample Output 0**

```
[[1 3]
 [2 4]]
[1 2 3 4]
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)