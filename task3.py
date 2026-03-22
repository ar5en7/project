def calculate(n):
    if n==0: return 0

    return n + calculate(n-1)

n = int(input("Enter the number:"))
print(calculate(n))