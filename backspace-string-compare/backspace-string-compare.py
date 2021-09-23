class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def check(val):
            ref = ""
            for i in val:
                if i == "#":
                    if ref != "":
                        ref =  ref[:-1]
                    elif ref == "":
                        pass
                else:
                    ref+=i
            return ref
        
        return check(s) == check(t)