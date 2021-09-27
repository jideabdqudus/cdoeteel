class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        max_so_far =a[0]
        curr_max = a[0]

        for i in range(1,len(a)):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)

        return max_so_far