# collections.deque()

https://www.hackerrank.com/challenges/py-collections-deque

### Problem

A deque is a double-ended queue. It can be used to add or remove elements from both ends.  
  
Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.  
  
Click on the link to learn more about deque() methods.   
Click on the link to learn more about various approaches to working with deques: Deque Recipes.  

**Task** 

Perform append, pop, popleft and appendleft methods on an empty deque d.  

**Input Format**

The first line contains an integer N, the number of operations.   
The next N lines contains the space separated names of methods and their values.  

**Output Format**

Print the space separated elements of deque d.

**Sample Input 0**

```
6
append 1
append 2
append 3
appendleft 4
pop
popleft
```

**Sample Output 0**

```
1 2
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)