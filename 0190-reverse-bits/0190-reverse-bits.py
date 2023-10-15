'''
Cesar Emilio Castaño Marin
Solution: Reverse Bits
Github username: CesarEmilioC
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #We define the new number that is going to be calculated
        num = 0
        for i in range(31,-1,-1):
            #Every power of 2 that is less than the current number, represents a 1 in the binary form
            if 2 ** i <= n:
                #We sum up the new power of two (like if the number was reversed)
                num += 2 ** (31 - i)
                #We update the number
                n -= 2 ** i
        return num
        