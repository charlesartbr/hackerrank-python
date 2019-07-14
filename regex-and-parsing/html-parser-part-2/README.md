# HTML Parser - Part 2

https://www.hackerrank.com/challenges/html-parser-part-2

**Task**

You are given an HTML code snippet of N lines.   
Your task is to print the single-line comments, multi-line comments and the data.  
  
Print the result in the following format:

```
>>> Single-line Comment  
Comment
>>> Data                 
My Data
>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:  
```

**Input format**

The first line contains integer N, the number of lines in the HTML code snippet.  
The next N lines contains HTML code.

**Output format**

Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.  
  
Format the answers as explained in the problem statement.  

**Sample Input 0**

```
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
```

**Sample Output 0**

```
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)