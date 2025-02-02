# Longest Palindromic Substring
```py
class Solution(object):
    def longestPalindrome(self, s):
        
        final = ''
        panindorme = lambda sub : sub == sub[::-1]
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if panindorme(s[i:j+1]) and (j-i+1>len(final)):
                    final = s[i:j+1]
        return final 
```
## Breakdown
### Declare ```final = ''``` As String
---
### Checking Palindrome 
```py
panindorme = lambda sub : sub == sub[::-1]
```
> take the original text compare with the reversed (ABC and CBA)
---
### Nest Loop
```py
        for i in range(len(s)):
            for j in range(i, len(s)):
```
> this will loop (eg. 01 02 0n 11 12 nn ... )
---
### Checking and Return back
```py
                if panindorme(s[i:j+1]) and (j-i+1>len(final)):
                    final = s[i:j+1]
        return final 
```
> What's happening 
- check if the original in that index and the reverse one the same or not
- check if it bigger than the previous longest string
- if both true then it'll store new string
---
## This's the easy way, here's for better time complexity [O(n)]()
```py
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
    
        T = "#" + "#".join(s) + "#"
        n = len(T)
        P = [0] * n  
        C, R = 0, 0  

        # Manacher's algorithm
        for i in range(n):
            mirror = 2 * C - i 
            if i < R:
                P[i] = min(R - i, P[mirror])
            while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]

        max_len, center_index = max((P[i], i) for i in range(n))
        start = (center_index - max_len) // 2  
        return s[start:start + max_len]

```
---
![bye](https://media.tenor.com/zlKoX5HPPu8AAAAM/cat-annoyed.gif)