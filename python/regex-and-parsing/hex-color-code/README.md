# Hex Color Code

https://www.hackerrank.com/challenges/hex-color-code

### Problem

CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).  

Specifications of HEX Color Code  

- It must start with a '#' symbol.
- It can have 3 or 6 digits.
- Each digit is in the range of 0 to F. (1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F).
- A - F letters can be lower case. (a, b, c, d, e and f are also valid digits).

**Input format**

The first line contains N, the number of code lines.
The next N lines contains CSS Codes.

**Output format**

Output the color codes with '#' symbols on separate lines.

**Sample Input 0**

```
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
```

**Sample Output 0**

```
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)