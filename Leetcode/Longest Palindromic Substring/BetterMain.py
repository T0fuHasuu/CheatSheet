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
