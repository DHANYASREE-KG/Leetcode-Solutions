class Solution(object):
    def minMergedInteger(self, nums):
        v=[]
        for i in range(0,len(nums),2):
            a=int(str(nums[i])+str(nums[i+1]))
            v.append(a)
        return min(v)

        