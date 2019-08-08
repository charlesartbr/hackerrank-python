# Validating Credit Card Numbers

https://www.hackerrank.com/challenges/validating-credit-card-number

### Problem

You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. 
You happen to be great at regex so he is asking for your help! 
  
A valid credit card from ABCD Bank has the following characteristics:   

- It must start with a 4, 5 or 6.   
- It must contain exactly 16 digits.   
- It must only consist of digits (0-9).   
- It may have digits in groups of 4, separated by one hyphen "-".   
- It must NOT use any other separator like ' ' , '_', etc.   
- It must NOT have 4 or more consecutive repeated digits.  

**Input Format**

The first line of input contains an integer N.   
The next N lines contain credit card numbers.

**Output Format**

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.  

**Sample Input 0**

```
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
```

**Sample Output 0**

```
Valid
Valid
Invalid
Valid
Invalid
Invalid
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)