# Check Strict Superset

https://www.hackerrank.com/challenges/py-check-strict-superset

**Problem**

You are given a set A and other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.  

A strict superset has at least one element that does not exist in its subset. 

**Input Format**

The first line contains the space separated elements of set A.  
The second line contains integer n, the number of other sets.  
The next n lines contains the space separated elements of the other sets. 

**Output Format**

Print True if set A is a strict superset of all other N sets. Otherwise, print False.

**Sample Input 0**

```
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
```

**Sample Output 0**

```
False
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)