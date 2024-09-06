class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0

        for num in nums:
            if num not in hashmap.keys():
                lcount = hashmap.get(num-1, 0)
                rcount = hashmap.get(num+1, 0)
                count = lcount + 1 + rcount

                hashmap[num] = count
                hashmap[num-lcount] = count
                hashmap[num+rcount] = count

                res = max(res, count)
        
        return res
                