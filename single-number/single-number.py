class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for item in nums:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        key_list = list(freq.keys()) 
        val_list = list(freq.values())
        print(key_list, val_list)
        return key_list[val_list.index(1)] 

        