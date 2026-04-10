def two_sum(arr, target):
    hashmap = {}
    
    for i, num in enumerate(arr):
        diff = target - num
        
        if diff in hashmap:
            return [hashmap[diff], i]
        
        hashmap[num] = i

arr = [2, 4, 70, 11, 5, 7, 15]
target = 9       

result = two_sum(arr, target)
print(f"Indices of the two numbers that add up to {target}: {result}")