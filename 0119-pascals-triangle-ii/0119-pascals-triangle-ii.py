'''
Cesar Emilio Castaño Marin
Solution: Pascal's Triangle II
Github Username: CesarEmilioC
'''
#We import the math library
from math import factorial
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #We generate the pascal row with combinatorics
        return [factorial(rowIndex)/(factorial(i)*factorial(rowIndex-i)) for i in range(rowIndex+1)]
    

        