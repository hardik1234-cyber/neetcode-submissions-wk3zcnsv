class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for x in nums:
            hashmap[x] = 1 + hashmap.get(x,0)
        
        for k,v in hashmap.items():
            if v > 1:
                return True
        return False