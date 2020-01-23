# Alternating Characters

https://www.hackerrank.com/challenges/alternating-characters/problem

You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.  

Your task is to find the minimum number of required deletions.  

For example, given the string s=AABAAB, remove an A at positions 0 and 3 to make S=ABAB in 2  deletions.  

**Function Description**  

Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.  

alternatingCharacters has the following parameter(s):  

- s: a string

**Input Format**  

The first line contains an integer q, the number of queries.  
The next q lines each contain a string s.  

**Constraints**  

Each string s will consist only of characters A and B  

**Output Format**  

For each query, print the minimum number of deletions required on a new line.  

**Sample Input**  

```
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
```

**Sample Output**  
```
3
4
0
0
4
```

### My Solution

- [Python](python.py)