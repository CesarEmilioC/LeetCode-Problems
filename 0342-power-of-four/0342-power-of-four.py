'''
Cesar Emilio Castaño Marin
Solution: Two Sum
Github Username: CesarEmilioC
Technique: Transform to binary and check the position of the 1
'''
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 4:
            if n == 1:
                return True
            else:
                return False
        else:
            numBin = bin(n)[2:]
            onePosition = numBin.index("1")
            try:
                numBin[onePosition+1:].index("1")
                return False
            except:
                pass
            if onePosition != len(numBin) - 1 and onePosition != len(numBin) - 2 and -(len(numBin) - onePosition) % 2 == 1:
                return True
            else:
                return False 

        