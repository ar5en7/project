def array(n,target,i=0):
    if len(n)==0:
        return "Not found"
    
    if n[0]==target:
        return "Found at index" +" "+str(i)
    else:
        return array(n[1:],target,i+1)
    
print(array([2,5,7,8],5))