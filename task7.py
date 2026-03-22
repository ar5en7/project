def calculate(n):
    if n<10: return 1
    return 1 + calculate(n//10)
n = int(input("Enter the number:"))
print(calculate(n))