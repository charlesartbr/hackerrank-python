# The Minion Game

https://www.hackerrank.com/challenges/the-minion-game

### Problem

Kevin and Stuart want to play the 'The Minion Game'.  
  
**Game Rules**  
Both players are given the same string, S.  
Both players have to make substrings using the letters of the string S.  
Stuart has to make words starting with consonants.  
Kevin has to make words starting with vowels.   
The game ends when both players have made all possible substrings.   

**Scoring**  
A player gets +1 point for each occurrence of the substring in the string S.  
  
**For Example:**  
String  = BANANA  
Kevin's vowel beginning word = ANA  
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.   

**Task** 

A single line of input containing the string S.   
Note: The string S will contain only uppercase letters: [A - Z].

**Input Format**

Print one line: the name of the winner and their score separated by a space.  
If the game is a draw, print Draw.

**Output Format**

Using any of the methods explained above, replace the character at index i with character c.

**Sample Input 0**

```
BANANA
```

**Sample Input 0**

```
Stuart 12
```

### My Solution

- [Python 2](python2.py)
- [Python 3](python3.py)