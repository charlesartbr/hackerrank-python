# XML 2 - Find the Maximum Depth

https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth

**Problem**

You are given a valid XML document, and you have to print the maximum level of nesting in it. 
Take the depth of the root as 0.

**Input Format**

The first line contains N, the number of lines in the XML document.
The next N lines follow containing the XML document.

**Output Format**

Output a single line, the integer value of the maximum level of nesting in the XML document.

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
1
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)