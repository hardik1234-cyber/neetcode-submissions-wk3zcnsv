class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for x,cnt in count.items():
            if cnt > (len(nums)/2):
                return x
