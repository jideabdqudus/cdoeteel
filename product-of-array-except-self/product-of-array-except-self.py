class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ref = []
        # for i in nums:
        #     val = nums.index(i)
        #     count = 1
        #     nums.pop(nums.index(i))
        #     for j in nums:
        #         count*=j
        #     nums.insert(val, i)
        #     ref.append(count)
        # return ref
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]
        return res