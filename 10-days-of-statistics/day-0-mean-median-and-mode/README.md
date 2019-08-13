# Day 0: Mean, Median, and Mode

https://www.hackerrank.com/challenges/s10-basic-statistics

### Problem

In this challenge, we practice calculating the mean, median, and mode. 

**Task**

Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3, 7.0 format).X

**Input Format**

The first line contains an integer, N, denoting the number of elements in the array. 
The second line contains N space-separated integers describing the array's elements.

**Output Format**

Print  lines of output in the following order:

- Print the mean on a new line, to a scale of 1 decimal place.
- Print the median on a new line, to a scale of 1 decimal place.
- Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

**Sample Input 0**

```
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
```

**Sample Output 0**

```
43900.6
44627.5
4978
```

### My Solution

- [Python (only built-in)](python.py)
- [Python (with numpy and scipy)](python-numpy-scipy.py)