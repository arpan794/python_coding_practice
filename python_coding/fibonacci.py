def fibonacci(n):
    result=[]
    a,b = 0,1
    for _ in range(n):
        result.append(a)
        a,b = b,a+b
    return result

result = fibonacci(5)
print(result)

