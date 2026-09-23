class Solution(object):
    def intersection(self, nums1, nums2):
        a=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                  a.append(i)
        return list(set(a))

