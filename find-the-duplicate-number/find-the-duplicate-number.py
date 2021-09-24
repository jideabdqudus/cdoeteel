class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ref = dict()
        for i in nums:
            try:
                if ref[i]:
                    ref[i]+=1
            except KeyError:
                ref[i] = 1
        max_key = max(ref, key=ref.get)
        return max_key