class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n=len(nums)
        a=[]
        for i in range(n):
            count=0
            for j in range(n):
                if nums[j]<nums[i]:
                    count+=1
            a.append(count)
        return a
        