class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maximum=0
        current=0
        for i in nums:
            if i==1:
                current+=1
                maximum=max(current,maximum)
            else:
                current=0
        return maximum



        