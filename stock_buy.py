class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        max=0
        for i in range(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
            else:
                profit=prices[i]-min
                if profit > max:
                    max=profit
        return max
