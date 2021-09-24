class Solution(object):
    def majorityElement(self, nums):
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
        print(max_key)
        return max_key

        