class Solution(object):
    def compress(self,chars):

        n=len(chars)
        i=0
        j=0
        while i<n:
            ch=chars[i]
            count=0
            while i<n and chars[i]==ch:
                count+=1
                i+=1
            chars[j]=ch
            j+=1
            if count>1:
                for digit in str(count):
                    chars[j]=digit
                    j+=1
    return j