# Day 1: Interquartile Range

https://www.hackerrank.com/challenges/s10-interquartile-range

### Problem

In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

**Task**

The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).

Given an array, X, of N integers and an array, F, representing the respective frequencies of X's elements, construct a data set, S, where each X occurs at frequency Fi. 
Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).

**Input Format**

The first line contains an integer, N, denoting the number of elements in arrays X and F.   
The second line contains N space-separated integers describing the respective elements of array X.   
The third line contains N space-separated integers describing the respective elements of array F.  

**Output Format**

Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of 1 decimal place (i.e., 12.3 format).

**Sample Input 0**

```
6
6 12 8 10 20 16
5 4 3 2 1 5
```

**Sample Output 0**

```
9.0
```

### My Solution

- [Python 2 (only built-in)](python2.py)
- [Python 3 (only built-in)](python3.py)
- [Python 3 (with numpy)](python3-numpy.py)