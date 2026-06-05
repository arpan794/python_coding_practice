# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr) // 2]
    
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
    
#     return quick_sort(left) + middle + quick_sort(right)


# # Example
# arr = [5, 3, 8, 4]
# print(quick_sort(arr))



# def partition(arr, low, high):

#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):

#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]

#     return i + 1


# def quick_sort(arr, low, high):

#     if low < high:

#         pivot_index = partition(arr, low, high)

#         quick_sort(arr, low, pivot_index - 1)
#         quick_sort(arr, pivot_index + 1, high)


# arr = [64, 34, 25, 12, 22, 11, 90]

# quick_sort(arr, 0, len(arr) - 1)

# print(arr)


def partition(arr, low, high):

    pivot = arr[low]

    i = low + 1
    j = high

    while True:

        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]

    return j


def quick_sort(arr, low, high):

    if low < high: 

        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


arr = [64, 34, 25, 12, 22, 11, 90]

quick_sort(arr, 0, len(arr) - 1)

print(arr)



# ⚔️ Merge vs Quick Sort (INTERVIEW GOLD)
# Feature	Merge Sort	Quick Sort
# Time	O(n log n)	O(n log n) avg
# Space	O(n) ❌	O(log n) ✅
# Stable	✅ Yes	❌ No
# Speed	Slower	Faster in practice 🔥
# 🧠 When to use what?
# Merge Sort → when stability matters
# Quick Sort → general purpose (most used)
# 🔥 Real-world Insight

# 👉 Python’s sorted() uses:

# Timsort (hybrid of merge + insertion)
# 🎯 Interview Answers (VERY IMPORTANT)
# Q: Why is Merge Sort O(n log n)?

# 👉 Because:

# log n → splitting
# n → merging
# Q: Why Quick Sort is faster?

# 👉 Because:

# In-place sorting
# Better cache usage
# Q: Biggest drawback?
# Merge → extra memory
# Quick → worst case O(n²)
# 🚀 Final Mental Model
# Bubble / Selection / Insertion → beginner
# Merge / Quick → real interview level