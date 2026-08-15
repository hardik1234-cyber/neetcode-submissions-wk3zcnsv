class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}

        for x in nums:
            hashset[x] = 1 + hashset.get(x,0)
        
        for val in hashset.values():
            if val > 1:
                return True
        return False