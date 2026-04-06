def linear_search (list, n):
    for i in list:
        if i == n :
            return True
    return -1

result = linear_search((2,5,4,3,8,7,6,4), 7)

if result == True:
    print("number found")
elif result == -1:
    print ("number not found")


#====================================================================================

def linear_search(lst, n):
    for index, value in enumerate(lst, start=1):
        if value == n:
            return index   # Add 1 to make it human-readable
    return -1  # Not found

result = linear_search((2, 5, 4, 3, 8, 7, 6, 4), 7)

if result != -1:
    print(f"Number found at position {result}")  # 1-based position
else:
    print("Number not found")
