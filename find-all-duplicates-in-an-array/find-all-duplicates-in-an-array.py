class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ref = dict()
        ans = []
        for i in nums:
            try:
                if ref[i]:
                    ref[i]+=1
            except:
                ref[i] = 1
        for i in ref:
            if ref[i] > 1:
                ans.append(i)
        return ans