class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_at_ele = defaultdict(int)
        res = 0

        for num in nums:
            if not len_at_ele[num]:
                len_at_ele[num] = len_at_ele[num-1] + len_at_ele[num+1] + 1
                len_at_ele[num - len_at_ele[num-1]] = len_at_ele[num]
                len_at_ele[num + len_at_ele[num+1]] = len_at_ele[num]
            
            res = max(res, len_at_ele[num])
        
        return res