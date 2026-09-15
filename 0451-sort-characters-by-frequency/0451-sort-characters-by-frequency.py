class Solution(object):
    def frequencySort(self, s):
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        item=list(freq.items())
        a=len(item)
        for i in range(a):
            for j in range(a-1):
                if item[j][1]<item[j+1][1]:
                    item[j],item[j+1]=item[j+1],item[j]
        char=""
        for ch,count in item:
            char+=ch*count
        return char