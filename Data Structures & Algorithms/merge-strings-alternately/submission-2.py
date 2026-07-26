class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        res = []
        i,j = 0,0

        while i<m or j < n:
            if i < m:
                res.append(word1[i])
            if j < n:
                res.append(word2[j])

            i += 1
            j +=1
        return "".join(res)