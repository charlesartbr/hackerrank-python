# Day 9: Multiple Linear Regression

https://www.hackerrank.com/challenges/s10-multiple-linear-regression

### Problem

**Objective**

In this challenge, we practice using multiple linear regression. Check out the Tutorial tab for learning materials!

**Task**

Andrea has a simple equation:

Y = a + b1 * f1 + b2 * f2 + ... + bm * fm

for (m + 1) real constants (a, f1, f2, ..., fm). We can say that the value of Y depends on m features. 
Andrea studies this equation for n different feature sets (f1, f2, f3, ..., fm) and records each respective value of Y. 
If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?

**Note:** You are not expected to account for bias and variance trade-offs.

**Input Format**

The first line contains 2 space-separated integers, m (the number of observed features) and n (the number of feature sets Andrea studied), respectively.  
Each of the n subsequent lines contain m + 1 space-separated decimals; the first m elements are features (f1, f2, f3, ..., fm), and the last element is the value of Y for the line's feature set.  
The next line contains a single integer, q, denoting the number of feature sets Andrea wants to query for.  
Each of the q subsequent lines contains m space-separated decimals describing the feature sets.

**Output Format**

For each of the q feature sets, print the value of Y on a new line (i.e., you must print a total of q lines).

**Sample Input**

```
2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18
```

**Sample Output**

```
105.22
142.68
132.94
129.71
```

**Explanation**

We're given m = 2, so Y = a + b1 * f1 + b2 * f2. 

We use the information above to find the values of a, b1, and b2. Then, we find the value of Y for each of the q feature sets.

### My Solution

- [Python 3](python3.py)
