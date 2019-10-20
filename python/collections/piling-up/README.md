# Piling Up!

https://www.hackerrank.com/challenges/piling-up

### Problem

There is a horizontal row of n cubes. 
The length of each cube is given. 
You need to create a new vertical pile of cubes. 
The new pile should follow these directions: if cube is on top of cube<sub>j</sub> then sideLength<sub>j</sub> > sideLength<sub>i</sub>.  

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print "Yes" if it is possible to stack the cubes. 
Otherwise, print "No". Do not print the quotation marks.

**Input Format**

The first line contains a single integer T, the number of test cases.  
For each test case, there are 2 lines.  
The first line of each test case contains n, the number of cubes.  
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

**Output Format**

For each test case, output a single line containing either "Yes" or "No" without the quotes.

**Sample Input 0**

```
2
6
4 3 2 1 3 4
3
1 3 2
```

**Sample Output 0**

```
Yes
No
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)