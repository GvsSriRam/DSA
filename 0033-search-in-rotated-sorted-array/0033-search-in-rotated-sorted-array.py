class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            
            if nums[l] <= nums[m]: # Mid point in continuous flow area
                if nums[l] <= target and target < nums[m]: # Target in that range of left to mid index
                    r = m-1
                else:
                    l = m+1
            else: # Mid point is in rotated area
                if target < nums[m] or target > nums[r]: # Target in rotated area
                    r = m-1
                else:
                    l = m+1
        return -1