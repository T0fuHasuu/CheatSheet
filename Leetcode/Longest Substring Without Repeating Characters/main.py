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
                
case = ['abcabcbb', 'bbbb', 'pwwkew']
    
for i in case:
    print(f"{i} : {Solution().lengthOfLongestSubstring(i)}")