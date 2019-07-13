# HTML Parser - Part 1

https://www.hackerrank.com/challenges/html-parser-part-1

### Problem

HTML  
Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

Parsing   
Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.

HTMLParser   
An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered.

**Task**

You are given an HTML code snippet of N lines. 
Your task is to print start tags, end tags and empty tags separately.

**Input format**

The first line contains integer N, the number of lines in a HTML code snippet.
The next N lines contain HTML code.

**Output format**

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.  
  
Use proper formatting as explained in the problem statement.

**Sample Input 0**

```
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
```

**Sample Output 0**

```
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)