# strong number
# Strong Number

# A number is a Strong Number if the sum of the factorials of its digits equals the number itself.

# Examples:

# 145 = 1! + 4! + 5!
#     = 1 + 24 + 120
#     = 145
# 40585 = 4! + 0! + 5! + 8! + 5!

# So:

# 145 → Strong Number
# 40585 → Strong Number

def fac(digit):
    if digit in (0,1):
        return 1
    return digit * fac(digit-1)

def strong_num(num):
    total = 0
    original = num
    while num > 0:
        digit = num % 10
        total += fac(digit)
        num //= 10

    return total == original

result = strong_num(145)

if result:
    print("No. is strong")
else:
    print("No. is not strong")


# optimize code

# For a Strong Number, digits are only 0-9.

# Instead of calculating factorial repeatedly, precompute them:


factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def strong_num(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total += factorials[digit]
        num //= 10

    return total == original