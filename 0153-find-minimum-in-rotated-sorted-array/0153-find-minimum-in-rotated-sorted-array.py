class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[r]
        while l<=r:
            m = (l+r)//2
            res = min(nums[l], nums[r], nums[m], res)
            if nums[l] > nums[m]:
                r = m-1
            else:
                l = m+1
        return res