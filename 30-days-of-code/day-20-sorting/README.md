# Day 20: Sorting

https://www.hackerrank.com/challenges/30-sorting

### Problem

**Objective**  

Today, we're discussing a simple sorting algorithm called Bubble Sort.

**Task**

Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. 

Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

**Input Format**

The first line contains an integer, n, denoting the number of elements in array a.
The second line contains n space-separated integers describing the respective values of a0, a1,...,an-1.

**Output Format**

Print the following three lines of output:

1. Array is sorted in numSwaps swaps, where numSwaps is the number of swaps that took place.
2. First Element: firstElement, where firstElement is the first element in the sorted array.
3. Last Element: lastElement, where lastElement is the last element in the sorted array.

**Sample Input 0**

```
3
1 2 3
```

**Sample Output 0**

```
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
```

**Sample Input 1**

```
3
3 2 1
```

**Sample Output 1**

```
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
```

### My Solution

- [Python 3](python3.py)