def sort(n,i=0):
    if i == len(n)-1: return "Sorted"

    if n[i] > n[i+1]: return "Not sorted"
    return sort(n,i+1)

print(sort([5,7,9,4]))
