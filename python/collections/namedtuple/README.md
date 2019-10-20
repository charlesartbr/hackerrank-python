# collections.namedtuple()

https://www.hackerrank.com/challenges/py-collections-namedtuple

### Problem

Basically, namedtuples are easy to create, lightweight object types.   
They turn tuples into convenient containers for simple tasks.   
With namedtuples, you don’t have to use integer indices for accessing members of a tuple. 

**Task** 

Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.  
  
Your task is to help Dr. Wesley calculate the average marks of the students.  

**Input Format**

The first line contains an integer N, the total number of students.   
The second line contains the names of the columns in any order.   
The next N lines contains the IDs, marks, class and name under their respective column names.

**Output Format**

Print the average marks of the list corrected to 2 decimal places.

**Sample Input 0**

TESTCASE 01
```
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
```

TESTCASE 02
```
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5 
```

**Sample Output 0**

TESTCASE 01
```
78.00
```

TESTCASE 02
```
81.00
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)