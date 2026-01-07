class Solution(object):
    def reverseWords(self, s):
       b=s.split()
       s1=[]
       for i in b:
           s1.append(i[::-1])
       r=" ".join(s1)
       return r