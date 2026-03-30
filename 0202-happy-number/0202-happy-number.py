class Solution(object):
    def isHappy(self, n):
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            total=0
            temp=n
            while temp>0:
                 digit=temp%10
                 total+=digit*digit
                 temp=temp//10
            n=total
        if n == 1:
            return True
        else:
            return False

        