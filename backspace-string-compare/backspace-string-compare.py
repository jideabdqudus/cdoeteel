def build_string(a):
    arr1 = list(a)
    empty_arr1 = []
    for x in range(len(arr1)):
        if arr1[x] == "#" and len(empty_arr1) > 0:
            empty_arr1.pop()
        else:
            empty_arr1.append(arr1[x])
    if "#" in empty_arr1:
        empty_arr1.remove("#")
    return empty_arr1


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        final_s = build_string(s)
        final_t = build_string(t)
        print(" ".join(final_s) == " ".join(final_t))
        return " ".join(final_s) == " ".join(final_t)
        
        