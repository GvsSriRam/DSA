class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in check.keys():
                return [check[diff], i]
            else:
                check[num] = i