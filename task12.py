def array(n):
    if len(n) == 1: return n[0]

    maximum = array(n[1::])

    if maximum < n[0]: return n[0]
    else: return maximum

print(array([2,5,9,6,7]))