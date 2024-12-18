class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ele_len_map = dict()
        nums_set = set(nums)

        res = 0

        for num in nums:
            if num - 1 in nums_set:
                continue
            start = num
            count = 0
            n = num
            while n in nums_set:
                count += 1
                n = n+1
            res = max(res, count)
        
        return res