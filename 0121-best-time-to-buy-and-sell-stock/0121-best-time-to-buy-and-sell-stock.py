class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        maxvalue=0
        minvalue=float('inf')
        for i in prices:
            minvalue=min(minvalue,i)
            profit=i-minvalue
            maxvalue=max(maxvalue,profit)
        return maxvalue