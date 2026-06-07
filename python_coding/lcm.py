# lcm 

def lcm(a,b):

    c, d= a, b
    
    while b != 0:
        a, b = b, (a%b)

    hcf = a

    lcm = (c*d) // hcf

    return lcm

print(lcm(12,18))