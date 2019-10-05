# Day 23: BST Level-Order Traversal

https://www.hackerrank.com/challenges/30-binary-trees

### Problem

**Objective**  

Today, we're going further with Binary Search Trees. 

**Task**

A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer, root, pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.  

Hint: You'll find a queue helpful in completing this challenge.

**Input Format**

The locked stub code in your editor reads the following inputs and assembles them into a BST:  
The first line contains an integer, T (the number of test cases).  
The T subsequent lines each contain an integer, data, denoting the value of an element that must be added to the BST.  

**Output Format**

Print the data value of each node in the tree's level-order traversal as a single line of  space-separated integers.

**Sample Input**

```
6
3
5
4
7
2
1
```

**Sample Output**

```
3 2 5 1 4 7 
```

### My Solution

- [Python 3](python3.py)