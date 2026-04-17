def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

nums = [12, 11, 13, 5, 6]
print(insertion_sort(nums))

# “Take one element and insert it in the correct position in sorted part”


# ⚔️ Selection vs Insertion (INTERVIEW GOLD)
# Feature	Selection Sort	Insertion Sort
# Approach	Find min & swap	Insert in correct place
# Swaps	Less	More shifts
# Best case	O(n²)	O(n) ✅
# Stable	❌ No	✅ Yes
# Use case	Rare	Small/partially sorted data
# 🎯 Final Intuition (Super Important)
# Selection Sort → “Find minimum and place it”
# Insertion Sort → “Insert element at correct position”
# 🧠 Interview Tip

# If asked:

# “Which is better?”

# 👉 Answer:

# Insertion Sort is better for nearly sorted arrays
# Selection Sort does fewer swaps