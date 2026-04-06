def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


# Example
arr = [5, 3, 8, 4]
print(quick_sort(arr))



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