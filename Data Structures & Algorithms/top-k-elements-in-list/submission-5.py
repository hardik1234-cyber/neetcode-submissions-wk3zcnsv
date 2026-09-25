class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = []
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for i in range(len(nums)+1):
            freq.append([])
        
        for nums,cnt in count.items():
            freq[cnt].append(nums)
        


        res = []

        for i in range(len(freq)-1,-1,-1):
            for nums in freq[i]:
                res.append(nums)
            if len(res) == k:
                return res
