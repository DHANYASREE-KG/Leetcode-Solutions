class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
       c=numBottles
       while numBottles>=numExchange:
          c1=numBottles//numExchange
          c+=c1
          numBottles=c1+numBottles%numExchange
       return c
        