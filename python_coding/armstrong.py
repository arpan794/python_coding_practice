# Armstrong Number
# A number is an Armstrong Number if the sum of its digits raised to the power of the number of digits equals the number itself.

# Examples:

# 153 = 1³ + 5³ + 3³ = 153
# 370 = 3³ + 7³ + 0³ = 370
# 371 = 3³ + 7³ + 1³ = 371
# 407 = 4³ + 0³ + 7³ = 407


def armstrong(num):
    total = 0
    digits = str(num)
    count = len(digits)
    
    for ch in digits:
        total += (int(ch)**count)

    return num == total

result = armstrong(9474)

if result:
    print("No. is armstrong")
else:
    print("Not a armstrong no.")


# Pure Mathematical Approach

def armstrong(num):
    temp = num

    count = 0
    while temp > 0:
        count += 1
        temp //= 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp //= 10

    return total == num
