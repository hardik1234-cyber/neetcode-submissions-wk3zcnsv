class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashset = {}

        for x in nums:
            hashset[x] = 1 + hashset.get(x,0)
        
        for value in hashset.values():
            if value > 1:
                return True
        return False
