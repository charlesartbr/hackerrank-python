# Merge the Tools!

https://www.hackerrank.com/challenges/merge-the-tools

### Problem

Consider the following:  

- A string, s, of length n where s=c<sub>0</sub>c<sub>1</sub>...c<sub>n</sub>-1.
- An integer, k, where k is a factor of n.

We can split s into n/k subsegments where each subsegment, t<sub>i</sub>, consists of a contiguous block of k characters in s. Then, use each t<sub>i</sub> to create string u<sub>i</sub> such that:

- The characters in u<sub>i</sub> are a subsequence of the characters in t<sub>i</sub>.
- Any repeat occurrence of a character is removed from the string such that each character in u<sub>i</sub> occurs exactly once. In other words, if the character at some index j in t<sub>i</sub> occurs at a previous index j in t<sub>i</sub>, then do not include the character in string u<sub>i</sub>.

Given s and k, print n/k lines where each line i denotes string u<sub>i</sub>.

**Input Format**

The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.

**Output Format**

Print n/k lines where each line i contains string u<sub>i</sub>.

**Sample Input 0**

```
AABCAAADA
3   
```

**Sample Output 0**

```
AB
CA
AD
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)