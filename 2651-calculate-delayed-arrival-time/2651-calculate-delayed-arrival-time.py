class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
       s=arrivalTime+delayedTime
       if s<=23:
         return s
       elif s>24:
         return s%24
       else:
         return 0
          
        