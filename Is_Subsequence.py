def is_subsquence(str1:str,str2:str)->bool:
    i=0
    j=0
    while i<len(str1) and j<len(str2):
        if str1[i]==str2[j]:
            i+=1   
            j+=1
        else:
            j+=1
    return i==len(str1)
#str1="abc"
#str2="ahbgdc"
#print(is_subsquence(str1,str2))