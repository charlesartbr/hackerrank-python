# No Idea!

https://www.hackerrank.com/challenges/no-idea

**Problem**

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. 
Your initial happiness is 0. 
For each i integer in the array, if i ϵ A, you add 1 to your happiness. 
If i ϵ B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

**Input Format**

The first line contains integers n and m separated by a space.  
The second line contains n integers, the elements of the array.  
The third and fourth lines contain m integers, A and B, respectively.

**Output Format**

Output a single integer, your total happiness.

**Sample Input 0**

```
3 2
1 5 3
3 1
5 7
```

**Sample Output 0**

```
1
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)