# Two Sum :
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]

# Add Two Numbers :
    def addTwoNumbers(self, l1, l2):
        
        # Build Node Structure
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Get value from l else 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # add value and carry
            total = val1 + val2 + carry
            carry = total //10
            digit = total % 10
            
            # Add to result
            current.next = ListNode(digit)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# Longest Substring Without Repeating Characters :
    def lengthOfLongestSubstring(self, s):
        start = 0
        seen = set()
        max_len = 0
        
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            max_len = max(max_len, end - start + 1)
        return max_len

# Median Two Sorted Array :
    def findMedianSortedArrays(self, nums1, nums2):
        combined = nums1 + nums2
        combined.sort()
        n = len(combined)
        if n % 2 == 1:
            return float(combined[n // 2])
        else:
            return (combined[n // 2 - 1] + combined[n // 2]) / 2.0

# Longest PalinDrome Substring :
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