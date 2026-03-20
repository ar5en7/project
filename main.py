def array(n):
    if len(n) == 1: return n[0]
    
    max = array(n[1::])

    if n[0] > max:
        return n[0]
    else:
        return max

print(array([4,9,1,7,3]))