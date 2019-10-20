# Set .union() Operation

https://www.hackerrank.com/challenges/py-set-union

**Problem**

The .union() operator returns the union of a set and the set of elements in an iterable.  
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.  
Set is immutable to the .union() operation (or | operation).

**Task**

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.  

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

**Input Format**

The first line contains an integer, n, the number of students who have subscribed to the English newspaper.  
The second line contains n space separated roll numbers of those students.  
The third line contains b, the number of students who have subscribed to the French newspaper.  
The fourth line contains b space separated roll numbers of those students. 

**Output Format**

Output the total number of students who have at least one subscription.  

**Sample Input 0**

```
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

**Sample Output 0**

```
13
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)