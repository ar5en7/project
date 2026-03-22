def calculate(n):
    if n<10: 
        print(n) 
        return 
    
    print(n%10,end=" ")
    calculate(n//10)

n = int(input("Enter the number:"))
calculate(n)