def sec_largest(number):
    
    first = float('-inf')
    second = float('-inf')
    for num in number:
        if num > first:
            second = first
            first = num
        elif num != first and num > second:
            second = num

    if second == float('-inf'):
        return "No second largest element"
    
    return second

# print(" 2nd largest no. is :", sec_largest([1,2,3,4,5,6,7,8]))

# ---- USER INPUT ----
nums = input("Enter numbers separated by space: ")

numbers = list(map(int, nums.split()))

print("Second largest number is:", sec_largest(numbers))