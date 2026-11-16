class Solution(object):
    def maxOperations(self,nums,k):
        nums.sort()
        l,r=0,len(nums)-1
        pairs=0
        while l<r:
            total=nums[l]+nums[r]

            if total==k:
                pairs+=1
                l+=1
                r-=1
            elif total<k:
                l+=1
            else:
                r-=1
        return pairs
