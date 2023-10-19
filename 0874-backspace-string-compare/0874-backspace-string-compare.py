class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = [char for char in s]
        while "#" in s[1:]:
            del s[s[1:].index("#"):s[1:].index("#")+2]
        t = [char for char in t]
        while "#" in t[1:]:
            del t[t[1:].index("#"):t[1:].index("#")+2]
        if len(s) >= 1:
            if s[0] == "#":
                del s[0]
        if len(t) >= 1:
            if t[0] == "#":
                del t[0]
        result = True if s == t else False
        return result
        

        

                
        
        