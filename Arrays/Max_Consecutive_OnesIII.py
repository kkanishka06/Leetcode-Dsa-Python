#BRUTE FORCE
#TIME COMPLEXITY->O(N^2)
def longestOnes(nums,k):
    max_length=0

    for i in range(len(nums)):
        zero_count=0

        for j in range(i,len(nums)):
            if nums[j]==0:
                zero_count+=1

            if zero_count<=k:
                length=j-i+1
                max_length=max(max_length,length)
            else:
                break
    return max_length

#BETTER VERSION
#TIME COMPLEXITY->O(2N)
def longestOnes(nums,k):
    l,r,zeroes,max_length=0,0,0,0
    while r<len(nums):
        if nums[r]==0:
            zeroes+=1
        while zeroes>k:
            if nums[l]==0:
                zeroes-=1
            l+=1
        if zeroes<=k:
            max_length=max(max_length,r-l+1)
            r+=1
    return max_length

#OPTIMIZED VERSION
#TIME COMPLEXITY-O(N)
def longestOnes(nums,k):
    l,r,zeroes,max_length=0,0,0,0
    for r in range(len(nums)):
        if nums[r]==0:
            zeroes+=1
        if zeroes>k:
            if nums[l]==0:
                zeroes-=1
            l+=1
        if zeroes<=k:
            max_length=max(max_length,r-l+1)
            r+=1
    return max_length
