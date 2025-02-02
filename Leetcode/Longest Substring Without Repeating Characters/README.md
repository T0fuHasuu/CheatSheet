# Longest Substring Without Repeating Characters
```py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char = set()
        left = 0
        maxL = 0
        
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            maxL = max(maxL, right - left + 1)
        return maxL
```
## Break Down
### Declare 
```py
        char = set()
        left = 0
        maxL = 0
```
> Variables
- **char** : set list for only not duplicated 
- **left** : scan if it's a duplicate with the far left and right
- **maxL** : store max lenght
---
### Loop
```py
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            maxL = max(maxL, right - left + 1)
```
> Functions 
- loop the amount of letters in **s**
- if the index letter is in the char list then it will delete the most left one so that it will add the index letter at the right while increment the left by 1 and move on
- if it's not in the char, it will the index letter to char
- store maximum number between maxL itself and result of sum
---
### Return
```py
        return maxL
```
> Alway return the value
---
![Byebye](https://media1.tenor.com/m/0x6FnOuQLRIAAAAC/cat-uni.gif)
