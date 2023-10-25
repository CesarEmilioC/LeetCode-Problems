'''
Cesar Emilio Castaño Marin
Solution: K-th Symbol in Grammar
Github Username: CesarEmilioC
Technique: Find the pattern in the tree formed by the table rows. Check half of the data
depending on k being greater than half the data using a recursive function.
'''
class Solution(object):

    def recursiveTreeCheck (self, k, pivot, n):
        print(k, pivot, n)
        if k > 2**(n-2):
            
            if pivot == 0:
                pivot = 1
            else:
                pivot = 0
            k -= 2**(n-2)
        else:
            if pivot == 0:
                pivot = 0
            else:
                pivot = 1
        n -= 1
        
        return k, pivot, n

    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        pivot = 0
        while n > 1:
            k, pivot, n = self.recursiveTreeCheck(k, pivot, n)
        return pivot

        