class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
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