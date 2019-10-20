# Default Arguments

https://www.hackerrank.com/challenges/default-arguments

**Problem**

In this challenge, the task is to debug the existing code to successfully execute all provided test files.  

Python supports a useful concept of default argument values. 
For each keyword argument of a function, we can assign a default value which is going to be used as the value of said argument if the function is called without it. 

**Input Format**

The input is read by the provided locked code template. 
In the first line, there is a single integer Q denoting the number of queries. 
Each of the following Q lines contains a stream_name followed by integer N, and it corresponds to a single test for your function.

**Output Format**

The output is produced by the provided and locked code template. 
For each of the queries (stream_name, n), if the stream_name is even then print_from_stream(n) is called. 
Otherwise, if the stream_name is odd, then print_from_stream(n, OddStream()) is called.

**Sample Input 0**

```
3
odd 2
even 3
odd 5
```

**Sample Output 0**

```
1
3
0
2
4
1
3
5
7
9
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)