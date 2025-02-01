# **Example**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next  

class Solution:
    def findNode(self, head, target):
        index = 0
        current = head  
        
        while current: 
            if current.val == target:
                return index 
            current = current.next  
            index += 1
        
        return -1  

node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2) 

solution = Solution()
print(solution.findNode(head, 3))  
print(solution.findNode(head, 5))  
```