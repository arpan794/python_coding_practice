def missing_number (nums):
    n = len(nums)+1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

nums = [1, 2, 3, 4, 5, 7]
print("Missing number is:", missing_number(nums))