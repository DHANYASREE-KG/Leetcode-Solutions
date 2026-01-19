class Solution(object):
    def pivotIndex(self, nums):
       t=sum(nums)
       left=0
       for i in range(len(nums)):
         if left == t-left-nums[i]:
            return i
         left=left+nums[i]
       return -1
        