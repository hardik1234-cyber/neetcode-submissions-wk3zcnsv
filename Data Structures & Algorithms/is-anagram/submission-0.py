class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        cs,ct = {},{}

        if len(s) != len(t):
            return False
        
        for x in s:
            cs[x] = 1 + cs.get(x,0)
        for x in t:
            ct[x] = 1 + ct.get(x,0)
        
        return cs == ct

