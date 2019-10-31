# Sherlock and Anagrams

https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

### Problem

Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example **s=mom**, the list of all anagrammatic pairs is **[m,m]**, **[mo,om]** at positions **[[0],[2]], [[0,1],[1,2]]** respectively.

**Function Description**  

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in **s**.  

sherlockAndAnagrams has the following parameter(s):

- s: a string

**Input Format**  

The first line contains an integer **q**, the number of queries.  
Each of the next **q** lines contains a string **s** to analyze.

**Output Format**

For each query, return the number of unordered anagrammatic pairs.  

**Sample Input 0**

```
2
abba
abcd
```

**Sample Output 0**

```
4
0
```

### My Solution

- [Python](python.py)