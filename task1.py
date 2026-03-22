def calculate(n):
    if n == 0: return 
    calculate(n-1)
    print(n,end=" ")
n = int(input("Enter the number:"))
calculate(n)
