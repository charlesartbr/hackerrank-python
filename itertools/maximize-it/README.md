# Maximize It!

https://www.hackerrank.com/challenges/maximize-it

### Problem

You are given a function f(x)=x<sup>2</sup>. You are also given K lists. The i<sup>th</sup> list consists of N<sub>i</sub> elements.

You have to pick one element from each list so that the value from the equation below is maximized: 

**S = (f(X<sub>1</sub>) + f(X<sub>2</sub>) + ... + f(X<sub>k</sub>)) % M**

X<sub>1</sub> denotes the element picked from the i<sup>th</sup> list. Find the maximized value S<sub>max</sub> obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

**Input Format**

The first line contains 2 space separated integers K and M. 
The next K lines each contains an integer N<sub>i</sub>, denoting the number of elements in the i<sup>th</sup> list, followed by N<sub>i</sub> space separated integers denoting the elements in the list.

**Output Format**

Output a single integer denoting the value S<sub>max</sub>.

**Sample Input 0**

```
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
```

**Sample Output 0**

```
206
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)