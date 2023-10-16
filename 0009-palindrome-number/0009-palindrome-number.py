'''
Cesar Emilio Castaño Marin
Solution: Palindrome Number
Github Username: CesarEmilioC
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #We transform the x number to an str object
        x = str(x)
        #We check if the reversed number is the same as x
        x_nuevo = x[::-1]
        if x_nuevo == x:
            return True
        else: 
            return False
        