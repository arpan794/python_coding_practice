# Product of Array Except Self

# Return an array where each element is the product of all elements except itself.

# Input: [1,2,3,4]
# Output: [24,12,8,6]

# * Prefix & suffix arrays
# * Optimization (no division)

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # prefix product
    prefix_product = 1
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= nums[i]

    # suffix product
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]

    return result