def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

nums = [64, 25, 12, 22, 11]
print(selection_sort(nums))



# “Find the smallest element and place it at the correct position”

# Think like this:

# 👉 You divide the array into:

# Left → sorted part
# Right → unsorted part

# 👉 Each time:

# Pick the minimum from unsorted
# Swap it with current position