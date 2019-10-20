# DefaultDict Tutorial

https://www.hackerrank.com/challenges/defaultdict-tutorial

### Problem

The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. 
If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want. 

**Input Format**

The first line contains integers, n and m separated by a space. 
The next n lines contains the words belonging to group A. 
The next m lines contains the words belonging to group B.

**Output Format**

Output m lines. 
The i<sup>th</sup> line should contain the 1-indexed positions of the occurrences of the i<sup>th</sup> word separated by spaces.

**Sample Input 0**

```
5 2
a
a
b
a
b
a
b
```

**Sample Output 0**

```
1 2 4
3 5
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)