def fac(num):
    fac = 1
    for n in range(1,num+1):
        fac *= n
    return fac

print("factorial of the no. is :",fac(5))