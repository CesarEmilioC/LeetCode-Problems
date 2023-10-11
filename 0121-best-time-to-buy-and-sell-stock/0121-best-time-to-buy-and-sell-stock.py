'''
Cesar Emilio Castaño Marin
Solution: Best time to buy and sell stock
Github Username: CesarEmilioC
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Special case
        if len(prices) == 1:
            return 0
        #First difference in the list
        difference = prices[1] - prices[0]
        #We define a variable to hold the minimum number until the index we are
        minimo = min(prices[:2])
        #Cycle to check the differences
        for i in range(2,len(prices)):
            #Check if there is a new maximum difference
            if prices[i] > prices[i-1]:
                if difference < prices[i] - minimo:
                    difference = prices[i] - minimo
            #If there is no a greater number than before, check if there is a new minimum
            else:
                minimo = min([minimo, prices[i]])
        #Return the difference if it is positive
        if difference > 0:
            return difference
        else:
            return 0
        