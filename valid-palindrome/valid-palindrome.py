class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        value = ''.join(item for item in s if item.isalnum()).lower()
        m, n = 0, len(value)-1
        if len(value) <=1: return True
        first_char = value[m]
        last_char = value[n]
        while m <= n:
            if first_char == last_char:
                m += 1
                n -= 1
                first_char = value[m]
                last_char = value[n]
            elif first_char != last_char:
                return False
        return True