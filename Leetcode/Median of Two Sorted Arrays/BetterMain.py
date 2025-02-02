class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):  
            nums1, nums2 = nums2, nums1 

        x, y = len(nums1), len(nums2)
        low, high = 0, x  

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX  

            # Get maxLeftX, minRightX
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            # Get maxLeftY, minRightY
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # If correct partition is found
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:  # Even length case
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:  # Odd length case
                    return float(max(maxLeftX, maxLeftY))
            
            elif maxLeftX > minRightY:  # Move partitionX to the left
                high = partitionX - 1  
            else:  # Move partitionX to the right
                low = partitionX + 1  
