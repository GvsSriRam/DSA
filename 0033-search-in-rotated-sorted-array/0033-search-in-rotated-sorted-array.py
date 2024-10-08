class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2

            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[m] == target:
                return m
            elif nums[m] > nums[l] and nums[m] > target and nums[l] < target:
                r = m-1
            elif nums[m] > nums[l] and nums[m] < target:
                l = m+1
            elif nums[m] < nums[l] and nums[m] > target:
                r = m-1
            elif nums[m] < nums[l] and target > nums[m] and target > nums[l]:
                r = m-1
            else:
                l = m+1
            
        return -1