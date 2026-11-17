#BRUTE FORCE
#TIME COMPLEXITY->O(N2)
def longestSubarrays(nums):
    n=len(nums)
    max_len=0
    for i in range(n):
        zeroes=0
        for j in range(i,n):
            if nums[j]==0:
                zeroes+=1
            if zeroes<=1:
                length=j-i+1
                max_len=max(max_len,length-1)
            else:
                break
    return max_len

#OPTIMISED VERSION
#TIME COMPLEXITY->O(N)
def longestSubarray(nums):
    l,zeroes,max_len=0,0,0
    for r in range(len(nums)):
        if nums[r]==0:
            zeroes+=1
        while zeroes>1:
            if nums[l]==0:
                zeroes-=1
            left+=1
        length=r-l+1
        max_len=max(max_len,length-1)
    return max_len
