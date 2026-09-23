class Solution(object):
    def majorityElement(self, nums):
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        item=list(count.items())
        for i in range(len(item)):
            for j in range(len(item)-i-1):
                if item[j][1]<item[j+1][1]:
                    item[j],item[j+1]=item[j+1],item[j]
        return item[0][0]
       
        