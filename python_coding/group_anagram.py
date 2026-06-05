# group anagram 

from collections import defaultdict

words = ["ate", "eat", "tea", "pet"]

# # group = defaultdict(list)

# group = {}

# for word in words:
#     key = "".join(sorted(word))
#     if key not in group:
#         group[key] = []
        
#     group[key].append(word)
    
    



group = defaultdict(list)

for word in words:
    key = "".join(sorted(word))
    
    group[key].append(word)

print(list(group.values()))


