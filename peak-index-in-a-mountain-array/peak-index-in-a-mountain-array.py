class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ref = 0
        for i in range(len(arr)):
            if arr[i] > ref:
                ref = arr[i]
        return arr.index(ref)