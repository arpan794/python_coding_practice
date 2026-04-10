def move_zeros(arr):
    j = 0  # position for non-zero
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    
    return arr

print(move_zeros([0, 1, 0, 3, 12]))