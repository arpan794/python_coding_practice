# rotate array by k steps

def rotate_array(arr,k):
    roatate = []

    while k > 0:
        roatate.append(arr[-1])
        arr.pop()
        k -= 1
    return roatate + arr

arr = [1,2,3,4,5]
k = 2   
print(rotate_array(arr, k))


# optimal solution

# arr = [1,2,3,4,5]
# k = 2

# n = len(arr)
# k = k % n

# arr.reverse()

# arr[:k] = reversed(arr[:k])
# arr[k:] = reversed(arr[k:])

# print(arr)