class Solution:

    def flatten(self, matrix):
        res = []

        for x in matrix:
            if type(x) == list:
                res.extend(self.flatten(x))
            else:
                res.append(x)

        return res

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = self.flatten(matrix)

        return target in flattened