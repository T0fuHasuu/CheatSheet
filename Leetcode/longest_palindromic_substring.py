class Solution(object):
    def longestPalindrome(self, s):
        def FindPaCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        Palindrome = ""
        for i in range(len(s)):
            oddP = FindPaCenter(i, i)
            evenp = FindPaCenter(i, i + 1)
            if len(oddP) > len(Palindrome):
                Palindrome = oddP
            if len(evenp) > len(Palindrome):
                Palindrome = evenp
        return Palindrome