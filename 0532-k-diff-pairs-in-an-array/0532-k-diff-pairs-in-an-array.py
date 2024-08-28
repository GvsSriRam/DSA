class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 1
        count = 0
        while i<len(nums) and j<len(nums):
            if i==j:
                j += 1
                continue
            diff = nums[j] - nums[i]
            if diff == k:
                x = nums[i]
                y = nums[j]
                count += 1
                while(i < len(nums) and nums[i] == x):
                    i += 1
                while(j < len(nums) and nums[j] == y): 
                    j += 1
            elif diff < k:
                j += 1
            else:
                i += 1
        
        return count