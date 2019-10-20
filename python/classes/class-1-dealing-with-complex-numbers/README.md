# Classes: Dealing with Complex Numbers

https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers

### Problem

For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.  

The real and imaginary precision part should be correct up to two decimal places.

**Input Format**

One line of input: The real and imaginary part of a number separated by a space.

**Output Format**

For two complex numbers C and D, the output should be in the following sequence on separate lines:  

- C + D
- C - D
- C * D
- C / D
- mod(C)
- mod(D)

For complex numbers with non-zero real (A) and complex part (B), the output should be in the following format:  

A + Bi

Replace the plus symbol (+) with a minus symbol (-) when B < 0.   

For complex numbers with a zero complex part i.e. real numbers, the output should be:  

A + 0.00i

For complex numbers where the real part is zero and the complex part is non-zero, the output should be:  

0.00 + Bi

**Sample Input 0**

```
2 1
5 6
```

**Sample Output 0**

```
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)