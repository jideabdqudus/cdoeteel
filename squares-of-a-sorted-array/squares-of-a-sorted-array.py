class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ref = []
        for i in nums:
            ref.append(i*i)
        ref.sort()
        return ref