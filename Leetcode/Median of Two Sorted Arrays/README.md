# Median of Two Sorted Arrays
```py
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        total = sorted(nums1 + nums2) 
        n = len(total)

        if n % 2 == 1:
            return float(total[n // 2])  
        else:
            return (total[n // 2 - 1] + total[n // 2]) / 2.0  
```
## Breakdown
### Merge & Sort
```py
        total = sorted(nums1 + nums2) 
        n = len(total)
```
---
> merge nums1 and nums2 together then sort it 
### Condition If
```py
        if n % 2 == 1:
            return float(total[n // 2])  
```
> If the amount length of total divided by 2 and has 1 remainder
- we take the middle index from the total list (eg, 9 take index 5)
---
### Condition Else
```py
        else:
            return (total[n // 2 - 1] + total[n // 2]) / 2.0  
```
> Else it will take the 2 middle index and divide by 2 as float
---
## Note : This is slow but easy, here is the more faster using [(O(log(m+n)))](https://github.com/T0fuHasuu/CheatSheet/blob/main/Leetcode/Median%20of%20Two%20Sorted%20Arrays/BetterMain.py)
___
![Byebye](https://media1.tenor.com/m/bMV3HjqQADQAAAAC/working-from-home.gif)
