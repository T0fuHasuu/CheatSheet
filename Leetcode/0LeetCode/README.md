# Romanian Clockwork : 
```py
s = "LVIII"
map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000
}
total = 0
x = 0
for char in s:
    x = map[char]
    total = total + x
print(total)   
```
# Checking Common Letter :
```py
strs = ["flower", "flow", "flight"]
sLetter = []
shortest_str = min(strs, key=len)
"""
    What this do is, it will check for the shortest string and then letall the element in the array 
    to start from index 0 and compare, if it the same it will add thatletter to the sLetter[].
    if not, it will break and end the loop.
"""
for i in range(len(shortest_str)):
    current_char = shortest_str[i]
    if all(s[i] == current_char for s in strs):
        sLetter.append(current_char)
    else:
        break
final = ''.join(sLetter)
print(final)
```
# Valid Parenthese :
```py
    def is_valid_parentheses(s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}                    # Mapping key
        for char in s:                                              # Count Every Letter in S
            if char in mapping:                                     # If there letter the same in mapping
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False                                    # if the letter are close parentheses, then return false
            else:
                stack.append(char)
        return not stack                                            # add to stack so that it can be use for closing paretheses in later on

    is_valid_parentheses("()[]{}")
```
# Merge and sort :
```py
    def MergeAndSort():
        list1 = [1,2,4]
        list2 = [1,3,4]
        
        total = []
        
        for item1 in list1:
            print(item1)
            total.append(item1)
        for item2 in list2:
            print(item2)
            total.append(item2)
        
        total.sort()
        return total
```
# Link list Merge and sort :
```py
    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution(object):
        def mergeTwoLists(self, list1, list2):
            """
            :type list1: Optional[ListNode]
            :type list2: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            dummy = ListNode()
            current = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next

            current.next = list1 if list1 else list2
            
            return dummy.next
```
# Duplicate checking :
```py
    class Solution(object):
        def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if not nums:
                return 0 

            k = 1
            
            for i in range(1, len(nums)):
                if nums[i] != nums[i - 1]: 
                    nums[k] = nums[i]  
                    k += 1
            return k  
```
# Remove Element :
```py
    class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```
# Finding Index :
```py
    def Index(self, haystack, needle):
        return haystack.find(needle)
```
# Search Insert Index :
```py
    <!-- Variable -->
    nums = [1, 3, 5, 6] 
    target = 5
    <!-- Main -->
    index = 0
    index = next((i for i in range(len(nums)) if nums[i] >= target), len(nums))
    return index
```
# Explicit Split :
```py
    def lengthOfLastWord(s):
        return len(s.strip().split()[-1])
```
# List Addition :
```py
    digits[-1] += 1 
    for i in range(len(digits) - 1, -1, -1):  
        if digits[i] >= 10: 
            digits[i] = 0
            if i == 0: 
                digits.insert(0, 1)
            else:
                digits[i - 1] += 1
    return digits
```
# Convert into Binary :
```py
    <!-- int(a, 2) meaning 2 is the binary and if chage to 10, it's decimal -->

    <!-- Main -->
    return bin(int(a, 2) + int(b, 2))[2:]
```
# Squre root without Built-in :
```py
    class Solution(object):
        def mySqrt(self, x):
            if x < 2:
                return x  itself.

            left, right = 0, x
            result = 0

            while left <= right:
                mid = (left + right) // 2 
                if mid * mid <= x:  
                    result = mid 
                    left = mid + 1 
                else:
                    right = mid - 1  

            return result
```
# Counting Possibility of step :
```py
    def Step(n):
        if n == 0:
        return 0
        if n == 1:
            return 1
        ways = [0] * (n + 1)
        ways[0] = 1
        ways[1] = 1
        for i in range(2, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]
```
# Remove Duplicate in sorted list :
```py
    # Basic Using Array

    def DuplicateRemover(head):
        print(head)
        Export = []
        for i in range(len(head)):
            if i == 0 or head[i] != head[i-1]:
                Export.append(head[i])
            else:
                continue
        return Export

    # Using Link List

    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
```
# Merging List U
```py
    # Using Basic 

    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums1.append(m)
        nums1.append(n)
        for i in range(len(nums2)):
            nums1.append(nums2[i])
            nums1.sort()
            while nums1[i] == nums1[i+1] or nums1[i] == 0:
                nums1.remove(nums1[i])
        
        return nums1

    # Using Pointer

    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:  
            return
        if m == 0:  
            nums1[:n] = nums2
            return

        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
```
# Binary Tree inorder Travelsal :
```py
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorderDFS(root):
            if root == None:
                return
            inorderDFS(root.left)
            res.append(root.val)
            inorderDFS(root.right)
            
        inorderDFS(root)
        return res
```
# Same tree :
```py
    def SameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```
# Symnastic :
```py
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root, root)
```
# MaxDepth :
```py
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if root is None:
            return 0

        Ldepth = self.maxDepth(root.left)
        Rdepth = self.maxDepth(root.right)
        
        return 1 + max(Ldepth, Rdepth)
```
# Add two numbers :
```py
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    class Solution(object):
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: Optional[ListNode]
            :type l2: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            # Dummy node to form the result list
            dummy = ListNode(0)
            current = dummy
            carry = 0
            
            # Traverse both lists
            while l1 or l2 or carry:
                # Get the values (0 if the node is None)
                val1 = l1.val if l1 else 0
                val2 = l2.val if l2 else 0
                
                # Calculate the sum and carry
                total = val1 + val2 + carry
                carry = total // 10
                new_digit = total % 10
                
                # Add the new digit to the result list
                current.next = ListNode(new_digit)
                current = current.next
                
                # Move to the next nodes in l1 and l2
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
            
            # Return the result list, skipping the dummy node
            return dummy.next
```
# Longest Substring Character :
```py
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            # Hash set to store unique characters in the current window
            char_set = set()
            max_length = 0
            start = 0

            for end in range(len(s)):
                # If the character is already in the set, move start to shrink the window
                while s[end] in char_set:
                    char_set.remove(s[start])
                    start += 1
                
                # Add the current character to the set
                char_set.add(s[end])

                # Update the maximum length
                max_length = max(max_length, end - start + 1)
            
            return max_length
```
# Median Sorted Array :
```py
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            middle1 = merged[n // 2 - 1]
            middle2 = merged[n // 2]
            return (middle1 + middle2) / 2.0
```