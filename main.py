def calculate(n):
    if n == 0: return 
    calculate(n-1)
    print(n,end=" ")
calculate(5)