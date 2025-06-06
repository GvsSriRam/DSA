from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_at_ele = defaultdict(int)
        res = 0
        for n in nums:
            if not len_at_ele[n]:
                len_at_ele[n] = len_at_ele[n-1] + len_at_ele[n+1] + 1
                len_at_ele[n - len_at_ele[n-1]] = len_at_ele[n]
                len_at_ele[n + len_at_ele[n+1]] = len_at_ele[n]
            res = max(res, len_at_ele[n])
        return res

