def prime (n):
    if n<=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for num in range( 3, int(n**0.5)+1, 2):
        if num % 2 == 0:
            return False
    
    return True

print(prime(-2))    