def calculate(n):
    if n<10: return n
    
    return n%10 + calculate(n//10)

n = int(input("Enter the number:"))
print(calculate(n))