'''
Cesar Emilio Castaño Marin
Solution: Longest Substring Without Repeating Characters
Github Username: CesarEmilioC
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Special cases
        if s == "":
            return 0
        elif len(s) == 1:
            return 1
        #We create a max lenght variable that is going to be updated in the loop
        max_lenght = 0
        for i in range(len(s)):
            substring = s[i]
            contador = 0
            #We check the substring with the largest lenght and without repeated symbols
            for letra in s[i+1:]:
                if letra not in substring:
                    substring += letra
                    contador += 1
                else:
                    break
            #We check if we have to update the max_lenght
            if max_lenght < len(substring):
                max_lenght = len(substring)
        return max_lenght