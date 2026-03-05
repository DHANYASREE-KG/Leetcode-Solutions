class Solution(object):
    def sortPeople(self, names, heights):
        a=len(heights)
        for i in range(a):
            for j in range(0,a-i-1):
                if heights[j]<heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
                    names[j],names[j+1]=names[j+1],names[j]
        return names


        