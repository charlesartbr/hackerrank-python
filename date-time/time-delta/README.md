# Time Delta

https://www.hackerrank.com/challenges/python-time-delta

### Problem

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. 
Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.  
  
Since sometimes posts are published and viewed in different time zones, this can be confusing. 
You are given two timestamps of one such post that a user can see on his newsfeed in the following format:  
  
Day dd Mon yyyy hh:mm:ss +xxxx  
  
Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

**Input Format**

The first line contains T, the number of testcases.   
Each testcase contains 2 lines, representing time t1 and time t2.  

**Output Format**

Print the absolute difference (t2 - t1) in seconds.

**Sample Input 0**

```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```

**Sample Output 0**

```
25200
88200
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)