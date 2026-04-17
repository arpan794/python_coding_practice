# 3. Find Intersection of Two Arrays
# Return common elements between two arrays.
# Input: [1,2,2,1], [2,2]
# Output: [2]

# def intersection(nums1, nums2):
#     set1 = set(nums1)
#     set2 = set(nums2)
    
#     return list(set1.intersection(set2))

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]  
# result = intersection(nums1, nums2)
# print("Intersection of the two arrays is:", result)



def intersection(nums1, nums2):
    seen = set(nums1)
    result = set()

    for num in nums2:
        if num in seen:
            result.add(num)
    return list(result)

nums1 = [1, 2, 2, 1]
nums2 = []
result = intersection(nums1, nums2)
print("Intersection of the two arrays is:", result)