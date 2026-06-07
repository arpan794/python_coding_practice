# perfect number
# Perfect Number

# A number is a Perfect Number if the sum of its proper divisors (excluding itself) equals the number.

# Examples:

# 6 = 1 + 2 + 3
# 28 = 1 + 2 + 4 + 7 + 14
# 496
# 8128

# So:

# 6 → Perfect Number
# 28 → Perfect Number

def perfect_num(num):
    total = 0
    for i in range(1,(num//2) + 1):
        if num % i == 0:
            total += i

    return total == num

result = perfect_num(8128)

if result:
    print("No. is perfect")
else:
    print("No. is not perfect")


# optimize code

# def perfect_num(num):

#     if num <= 1:
#         return False

#     divisor_sum = 1

#     for i in range(2, int(num ** 0.5) + 1):

#         if num % i == 0:

#             divisor_sum += i

#             other_factor = num // i

#             if other_factor != i:
#                 divisor_sum += other_factor

#     return divisor_sum == num