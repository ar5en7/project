def calculate(n, target):
    if len(n) == 0:
        return "Not found"

    if target == n[0]:
        return "Found"
    else:
        return calculate(n[1:], target)


print(calculate([2,5,6,4,8],9))