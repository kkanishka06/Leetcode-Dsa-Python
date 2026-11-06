class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        greatest=max(candies)
        result=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=greatest:
                result.append(True)
            else:
                result.append(False)
        return result
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        