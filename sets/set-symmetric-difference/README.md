# Set .symmetric_difference() Operation

https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation

**Problem**

The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.  
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.  
The set is immutable to the .symmetric_difference() operation (or ^ operation).

**Task**

Students of District College have subscriptions to English and French newspapers. 
Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.  

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.  

**Input Format**

The first line contains the number of students who have subscribed to the English newspaper.   
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.  
The third line contains the number of students who have subscribed to the French newspaper.   
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.  

**Output Format**

Output total number of students who have subscriptions to the English or the French newspaper but not both.

**Sample Input 0**

```
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

**Sample Output 0**

```
8
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)