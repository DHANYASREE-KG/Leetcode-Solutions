class Solution(object):
    def restoreString(self, s, indices):
       a=[]
       for i in range(len(s)):
         for j in range(len(indices)):
            if indices[j]==i:
               a.append(s[j])
               break
       return ''.join(a)
       
         
           
       