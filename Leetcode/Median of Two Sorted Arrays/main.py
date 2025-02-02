class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        total = sorted(nums1 + nums2) 
        n = len(total)

        if n % 2 == 1:
            return float(total[n // 2])  
        else:
            return (total[n // 2 - 1] + total[n // 2]) / 2.0  

"""Test Case"""
case = [
    ([1,3],[2]),
    ([1,2],[3,4])
]
for i in case:
    print(f"Median of {i} : {Solution().findMedianSortedArrays(*i)}")