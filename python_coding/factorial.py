def fac(num):
    fac = 1
    for n in range(1,num+1):
        fac *= n
    return fac

print("factorial of the no. is :",fac(0))


# factorial recursive

# def fac(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fac(num-1)
    
# print("factorial of the no. is :",fac(0))