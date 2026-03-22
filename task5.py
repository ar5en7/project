def power(x,y):
    if y==0: return 1

    return x*(x**(y-1))

x = int(input("Enter the number:"))
y = int(input("Enter the power of numbe:"))

print(power(x,y))