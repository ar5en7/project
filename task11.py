def array(n):
    if len(n) == 0: return 0
    return n[0] + array(n[1::])

print(array([2,4,9,3]))