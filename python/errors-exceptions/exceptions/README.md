# Exceptions

https://www.hackerrank.com/challenges/exceptions

### Problem

Errors detected during execution are called exceptions.

**Task**

You are given two values a and b.   
Perform integer division and print a/b.

**Input Format**

The first line contains T, the number of test cases.   
The next T lines each contain the space separated values of a and b.

**Output Format**

Print the value of a/b.   
In the case of ZeroDivisionError or ValueError, print the error code.

**Sample Input 0**

```
3
1 0
2 $
3 1
```

**Sample Output 0**

```
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)