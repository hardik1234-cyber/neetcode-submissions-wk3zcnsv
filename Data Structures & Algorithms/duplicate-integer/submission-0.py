class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}

        for x in nums:
            hashset[x] = 1 + hashset.get(x,0)
        
        for v in hashset.values():
            if v == 2:
                return True
        return False
