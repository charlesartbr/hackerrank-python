# Day 17: More Exceptions

https://www.hackerrank.com/challenges/30-more-exceptions

### Problem

**Objective**  

Yesterday's challenge taught you to manage exceptional situations by using try and catch blocks. In today's challenge, you're going to practice throwing and propagating an exception.

**Task**

Write a Calculator class with a single method: int power(int,int). 
The power method takes two integers, n and p, as parameters and returns the integer result of n<sup>p</sup>. 
If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.

Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.  

**Input Format**

Input from stdin is handled for you by the locked stub code in your editor. 
The first line contains an integer, T, the number of test cases. Each of the T subsequent lines describes a test case in 2 space-separated integers denoting n and p, respectively.

**Output Format**

Output to stdout is handled for you by the locked stub code in your editor. 
There are T lines of output, where each line contains the result of n<sup>p</sup> as calculated by your Calculator class' power method.

**Sample Input**

```
4
3 5
2 4
-1 -2
-1 3
```

**Sample Output**

```
243
16
n and p should be non-negative
n and p should be non-negative
```

### My Solution

- [Python 3](python3.py)