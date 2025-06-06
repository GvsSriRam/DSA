class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num_idx = dict()

        for i, n in enumerate(nums):
            if target-n in seen_num_idx.keys():
                return [i, seen_num_idx.get(target-n)]
            seen_num_idx[n] = i
