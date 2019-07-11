# Re.findall() & Re.finditer()

https://www.hackerrank.com/challenges/re-findall-re-finditer

### Problem

re.findall()  
The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.   
  
re.finditer()  
The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 

**Task**
 
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).   
Your task is to find all the substrings of S that contains 2 or more vowels.   
Also, these substrings must lie in between 2 consonants and should contain vowels only.

**Input format**

A single line of input containing string S.

**Output Format**

Print the matched substrings in their order of occurrence on separate lines.   
If no match is found, print -1.

**Sample Input 0**

```
rabcdeefgyYhFjkIoomnpOeorteeeeet
```

**Sample Output 0**

```
ee
Ioo
Oeo
eeeee
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)