def calculate(n):
    if n == 0: return 
    print(n,end=" ")
    calculate(n-1)
calculate(5)