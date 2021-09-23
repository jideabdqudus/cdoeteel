class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for x in range(0, len(nums)):
            try:
                currentVal = dict[nums[x]] # Check if there's the element in dict
                print([currentVal, x])
                return [currentVal, x]
            except KeyError:
                numberToFind = target - nums[x]
                dict[numberToFind] = x
        print("None")
        return None 