class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            a=i
            for j in range(i+1,n):
                if nums[j]<nums[a]:
                    a=j
            nums[i],nums[a]=nums[a],nums[i]
        return nums