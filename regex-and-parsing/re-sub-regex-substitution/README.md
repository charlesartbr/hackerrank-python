# Regex Substitution

https://www.hackerrank.com/challenges/re-sub-regex-substitution

### Problem

The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).  
The method is called for all matches and can be used to modify strings in different ways.  
The re.sub() method returns the modified string as an output.

**Task**

You are given a text of N lines. The text contains && and || symbols.  
Your task is to modify those symbols to the following:  

```
&& → and
|| → or
```

Both && and || should have a space " " on both sides.

**Input format**

The first line contains the integer, N.
The next N lines each contain a line of the text.

**Output format**

Output the modified text.

**Sample Input 0**

```
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
```

**Sample Output 0**

```
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)