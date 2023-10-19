'''
Cesar Emilio Castaño Marin
Solution: Backspace String Compare
Github Username: CesarEmilioC
Technique: Eliminate adjacent pairs in string turned into list
'''
class Solution(object):
    #Function to create new string only with the remain characters
    def eliminateAdjacent(self, word):
        word = [char for char in word]
        while "#" in word[1:]:
            del word[word[1:].index("#"):word[1:].index("#")+2]
        if len(word) >= 1:
            if word[0] == "#":
                del word[0]
        return word
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Compare words
        s = self.eliminateAdjacent(s)
        t = self.eliminateAdjacent(t)
        result = True if s == t else False
        return result
        

        

                
        
        