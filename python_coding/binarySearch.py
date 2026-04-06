def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid          # ✅ index is returned
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1                  # ❌ only if not found


# ---- DRIVER CODE ----
nums = [2, 1, 3, 4, 5, 6]
nums.sort()                     # IMPORTANT
target = 4

index = binary_search(nums, target)

if index != -1:
    print(f"Number found at index {index} in sorted list {nums}")
else:
    print("Number not found")
