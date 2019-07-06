Collections.OrderedDict()

https://www.hackerrank.com/challenges/py-collections-ordereddict

### Problem

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. 
If a new entry overwrites an existing entry, the original insertion position is left unchanged.

**Task** 

You are the manager of a supermarket.   
You have a list of N items together with their prices that consumers bought on a particular day.   
Your task is to print each item_name and net_price in order of its first occurrence.  
  
item_name = Name of the item.   
net_price = Quantity of the item sold multiplied by the price of each item.  

**Input Format**

The first line contains the number of items, N.   
The next N lines contains the item's name and price, separated by a space.

**Output Format**

Print the item_name and net_price in order of its first occurrence.

**Sample Input 0**

```
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
````

**Sample Output 0**

```
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)