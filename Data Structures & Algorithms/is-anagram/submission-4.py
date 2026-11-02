class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs , ct = {},{}

        for x in s:
            cs[x] = 1 + cs.get(x,0)
        for y in t:
            ct[y] = 1 + ct.get(y,0)
        
        return cs == ct