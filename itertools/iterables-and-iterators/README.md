# Iterables and Iterators

https://www.hackerrank.com/challenges/iterables-and-iterators

### Problem

The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.  
Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.  
  
You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.  

Find the probability that at least one of the K indices selected will contain the letter: 'a'.  

**Input Format**

The input consists of three lines. 
The first line contains the integer N, denoting the length of the list. 
The next line consists of space-separated lowercase English letters, denoting the elements of the list.  
  
The third and the last line of input contains the integer K, denoting the number of indices to be selected.

**Output Format**

Output a single line consisting of the probability that at least one of the K indices selected contains the letter: 'a'.  
  
Note: The answer must be correct up to 3 decimal places.

**Sample Input 0**

```
4 
a a c d
2
```

**Sample Output 0**

```
0.8333
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)