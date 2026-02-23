class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = dict()
        for i in range(len(nums)):
            search_val = target - nums[i]
            if search_val in idx:
                return [i, idx[search_val]]
            idx[nums[i]] = i
        return []
