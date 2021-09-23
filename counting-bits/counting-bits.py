class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, n+1, 1):
            li = bin(i)
            ans.append(li[2:])
        ref=[]
        j = 0
        for elem in ans:
            j = 0
            if len(elem) > 1:
                for i in elem:
                    j+= int(i)
                ref.append(j)
                j=0
            else:
                ref.append(int(elem))
        return ref