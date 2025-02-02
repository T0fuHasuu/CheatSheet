class Solution(object):
    def longestPalindrome(self, s):
        
        final = ''
        panindorme = lambda sub : sub == sub[::-1]
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if panindorme(s[i:j+1]) and (j-i+1>len(final)):
                    final = s[i:j+1]
        return final 

"""Case Test"""
case = ['babad', 'cbbd']
for i in case:
    print(f"[Case {i}] : {Solution().longestPalindrome(i)}")

