class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s=0
        temp=x
        while(temp>0):
           digit=temp%10
           s=s*10+digit
           temp=temp//10
        if x==s:
            return True
        else:
            return False
        
