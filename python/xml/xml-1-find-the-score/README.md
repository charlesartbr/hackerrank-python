# XML 1 - Find the Score

https://www.hackerrank.com/challenges/xml-1-find-the-score

**Problem**

You are given a valid XML document, and you have to print its score. 
The score is calculated by the sum of the score of each element. 
For any element, the score is equal to the number of attributes it has.

**Input Format**

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

**Output Format**

Output a single line, the integer score of the given XML document.

**Sample Input 0**

```
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
```

**Sample Output 0**

```
5
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)