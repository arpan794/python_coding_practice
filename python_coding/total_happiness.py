# Input Format

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, a and b, respectively.

# Output Format

# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output

# 1
# Explanation

# You gain 1 unit of happiness for elements 3 and 1 in set a. You lose 1 unit for element 5 in set b. The element 7 in set b does not exist in the array so it is not included in the calculation.

# Hence, the total happiness is 2-1 = 1.

def total_happiness(arr,setA,setB):
    
    happiness = 0

    for i in arr:
        if i in setA:
            happiness +=1
        elif i in setB:
            happiness -=1
    print(happiness)



arr = list(map(int, input().split()))

setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

total_happiness(arr,setA,setB)

