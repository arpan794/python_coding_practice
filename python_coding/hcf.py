# calculate HCF 

# def hcf(a,b):

#     com_fact = []

#     for i in range(1, min(a,b)+1):
#         if a % i == 0 and b % i == 0:
#             com_fact.append(i)
#     return max(com_fact)

# result = hcf(12,18)

# print("HCF of no. is :", result)


def hcf(a, b):

    hcf_val = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            hcf_val = i

    return hcf_val

print(hcf(12, 18))


# max optimize Euclidean Algorithm (HCF/GCD)

# def hcf(a, b):

#     while b != 0:
#         a, b = b, a % b

#     return a

# print(hcf(12, 18))


