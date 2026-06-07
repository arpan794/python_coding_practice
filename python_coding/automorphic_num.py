# Method 1: String Approach (Easy)
# def automorphic(num):
#     square = num * num

#     return str(square).endswith(str(num))


# result = automorphic(76)

# if result:
#     print("Automorphic Number")
# else:
#     print("Not an Automorphic Number")


# Method 2: Mathematical Approach (Optimized)

def automorphic(num):

    square = num * num
    temp = num

    while temp > 0:

        if temp % 10 != square % 10:
            return False

        temp //= 10
        square //= 10

    return True


result = automorphic(76)

if result:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")