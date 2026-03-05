class Solution(object):
    def sortedSquares(self, nums):
        f=list(map(lambda n:n**2,nums))
        f.sort()
        return f
        