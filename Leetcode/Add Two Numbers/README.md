# Add Two Number
```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
```
---
## Breakdown
### Here is [Linknode](https://github.com/T0fuHasuu/CheatSheet/blob/main/Leetcode/Add%20Two%20Numbers/ListNode.md) Example
### Initialize
```py
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
> Setting Variables
---
### Declare
```py
        dummy = ListNode()
        current = dummy
        carry = 0
```
> Make **Dummy** as Link list & **Carry** (Second Digit After Sum)
---
### Loop Condition 
```py
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
```
> while there value in **l1, l2 and carry** :
- will take value from them unless 0 for None
- create new **total** to store the summation
- Take only the second digit (Eg. 42, carry is 4)
- Take remainder by 10
- make the previous node to the next node
---
### Return
```python
        return dummy.next
```
> Always return values
---
![byebye](https://media1.tenor.com/m/RvFKEEqUpnIAAAAC/deep-sea-creature-sea-creature.gif)