def array(n,target):
    if len(n) == 0: return 0

    if n[0] == target: return 1 + array(n[1:],target)
    else: return array(n[1:],target)

    print(array([2,5,7,8,7],2))