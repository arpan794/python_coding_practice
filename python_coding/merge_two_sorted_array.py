
def merge_sorted_arrays(arr1, arr2):
    if arr1 == []:
        return arr2
    if arr2 == []:
        return arr1
    
    merged_arr = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    # Add remaining elements
    merged_arr.extend(arr1[i:])
    merged_arr.extend(arr2[j:])
    return merged_arr

# Example usage
arr1 = []     
arr2 = [2, 4, 6, 8]
merged = merge_sorted_arrays(arr1, arr2)
print("Merged sorted array:", merged)