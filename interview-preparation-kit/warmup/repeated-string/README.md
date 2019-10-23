# Repeated String

https://www.hackerrank.com/challenges/repeated-string/problem

### Problem

Lilah has a string, **s**, of lowercase English letters that she repeated infinitely many times.  

Given an integer, **n**, find and print the number of letter a's in the first  letters of Lilah's infinite string.  

For example, if the string **s='abcac'** and **n=10**, the substring we consider is **abcacabcac**, the first **10** characters of her infinite string. There are **4** occurrences of a in the substring.  

**Function Description**  

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

- s: a string to repeat
- n: the number of characters to consider

**Input Format**

The first line contains an integer **n**, the number of socks represented in **ar**.
The second line contains **n** space-separated integers describing the colors **ar[i]** of the socks in the pile.

**Output Format**

Print a single integer denoting the number of letter a's in the first **n** letters of the infinite string created by repeating  infinitely many times.

**Sample Input 0**

```
aba
10
```

**Sample Output 0**

```
7
```

### My Solution

- [Python](python.py)