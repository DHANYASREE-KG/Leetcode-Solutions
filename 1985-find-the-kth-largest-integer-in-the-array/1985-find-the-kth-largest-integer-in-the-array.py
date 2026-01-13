class Solution(object):
    def kthLargestNumber(self, nums, k):
       nums.sort(key=int)
       return nums[-k]
        