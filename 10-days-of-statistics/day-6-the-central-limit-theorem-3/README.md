# Day 6: The Central Limit Theorem III

https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3

### Problem

In this challenge, we practice solving problems based on the Central Limit Theorem. 

**Task**

You have a sample of 100 values from a population with mean µ=500 and with standard deviation σ=80.   

Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A < x < B) = 0.95.   

Use the value of z=1.96. Note that z is the z-score.  

**Input Format**

There are five lines of input (shown below):

```
100
500
80
.95
1.96
```

The first line contains the sample size.   
The second and third lines contain the respective mean (µ) and standard deviation (σ).   
The fourth line contains the distribution percentage we want to cover (as a decimal), and the fifth line contains the value of z.  


**Output Format**

Print the following two lines of output, rounded to a scale of 2 decimal places (i.e., 1.23 format):  

1. On the first line, print the value of A.  
2. On the second line, print the value of B.  

### My Solution

- [Python 3](python3.py)
