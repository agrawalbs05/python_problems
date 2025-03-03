# Best time to buy and sell stock
# Tags: N121, Blind75, sliding window, array,Easy  

def maxProfit(prices):
        max_profit = 0
        #Set min price to first element in array
        min_price = prices[0]
        #loop from second element
        for i in range(1,len(prices)):
            min_price =  min(min_price,prices[i])
            max_profit = max(max_profit,prices[i]-min_price)
            
        return max_profit
        
prices = [7,1,5,3,6,4]
maxProfit(prices)