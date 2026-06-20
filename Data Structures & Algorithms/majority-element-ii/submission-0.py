class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        counts = {}

        for x in nums:
            counts[x] = 1 + counts.get(x,0)
        
        for k,v in counts.items():
            if v > len(nums)/3:
                res.append(k)
        return res