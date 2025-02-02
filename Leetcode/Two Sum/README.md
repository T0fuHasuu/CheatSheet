# Answer 
```python
class Solution:

    # def __init__(self, nums, target):
    #     self.nums = nums
    #     self.target = target
    
    def twoSum(self, nums, target):
        for i in range(len(nums)):  
            for j in range(i + 1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i, j]  
        return [] 

```
---
> How it works 
1. **For loop** to get the index **i**
2. **Nest loop** to get the index **j** but have it start from index 1
3. **IF** so that if the value ``index (i) + index (j) == target``
- it will return values as index

## You can Test Code [Here](https://github.com/T0fuHasuu/CheatSheet/blob/main/Leetcode/Two%20Sum/main.py)

![HappyHappy](https://imgs.search.brave.com/uFBUxZssIwUSr6vrHT74PRixVdzpgOAL9LbfblWSMMo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9naWZk/Yi5jb20vaW1hZ2Vz/L2hpZ2gvaGFwcHkt/am9sbHktanVtcGlu/Zy1jYXQtbWVtZS1k/cm5qem5qeXJtcGpp/YmV5LmdpZg.gif)
