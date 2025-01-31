class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twosum(self):
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j] 
        return []



# Test 3 cases
case = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6)
]
# Loop for answers
for i, (nums, target) in enumerate(case, 1):
    print(f"Case {i} : {Solution(nums, target).twosum()}")