class Solution(object):
    def lengthOfLongestSubstring(self, s):
      a=len(s)
      max_length=0
      for i in range(a):
        d=[]
        for j in range(i,a):
            if s[j] in d:
                break
            else:
                d.append(s[j])
            length=j-i+1
            max_length=max(max_length,length)
      return max_length
         

        


        