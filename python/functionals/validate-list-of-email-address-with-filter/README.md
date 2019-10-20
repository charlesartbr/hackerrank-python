# Validating Email Addresses With a Filter

https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

### Problem

You are given an integer N followed by N email addresses.   
Your task is to print a list containing only valid email addresses in lexicographical order.

Valid email addresses must follow these rules:

- It must have the username@websitename.extension format type.
- The username can only contain letters, digits, dashes and underscores.
- The website name can only have letters and digits.
- The maximum length of the extension is . 

**Input Format**

The first line of input is the integer N, the number of email addresses.   
N lines follow, each containing a string.

**Output Format**

Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].

**Sample Input 0**

```
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
```

**Sample Output 0**

```
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)