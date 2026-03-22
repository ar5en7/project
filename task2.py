def calculate(n):
    if n==0:
        return 
    print(n,end=" ")
    return calculate(n-1)

n = int(input("Enter the number:"))
calculate(n)