# Day 24: More Linked Lists

https://www.hackerrank.com/challenges/30-linked-list-deletion

### Problem

**Task**

A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in a list).  

A removeDuplicates function is declared in your editor, which takes a pointer to the head node of a linked list as a parameter. Complete removeDuplicates so that it deletes any duplicate nodes from the list and returns the head of the updated list.  

Note: The head pointer may be null, indicating that the list is empty. Be sure to reset your next pointer when performing deletions to avoid breaking the list.

**Input Format**

You do not need to read any input from stdin. The following input is handled by the locked stub code and passed to the removeDuplicates function:  
The first line contains an integer, N, the number of nodes to be inserted.  
The N subsequent lines each contain an integer describing the data value of a node being inserted at the list's tail.

**Output Format**

Your removeDuplicates function should return the head of the updated linked list. The locked stub code in your editor will print the returned list to stdout.

**Sample Input**

```
6
1
2
2
3
3
4
```

**Sample Output**

```
1 2 3 4 
```

### My Solution

- [Python 3](python3.py)