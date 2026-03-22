def palindrome(n):
    if len(n)<=1:
        return "Palindrome"
    if n[0] != n[-1]:
        return "Not palindrome"
    
    return palindrome(n[1:-1])

n = input("Enter the word:")
print(palindrome(n))