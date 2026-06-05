def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


num = 29

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")   


# print all the prime numbers up to n

# def print_primes(n):

#     for num in range(2, n + 1):

#         is_prime = True

#         for i in range(2, int(num ** 0.5) + 1):

#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print(num, end=" ")


# print_primes(20)