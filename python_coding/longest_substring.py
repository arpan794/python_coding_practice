# def longest_non_repeating_substring(s):
#     char_index = {}
#     start = 0
#     max_length = 0
#     longest_substring = ""

#     for end, ch in enumerate(s):
#         if ch in char_index and char_index[ch] >= start:
#             start = char_index[ch] + 1
#         char_index[ch] = end
#         current_length = end - start + 1
#         if current_length > max_length:
#             max_length = current_length
#             longest_substring = s[start:end+1]

#     return longest_substring

# s = "abcabcdbb"
# result = longest_non_repeating_substring(s)
# print("Longest non-repeating substring is:", result)


s = "abcabcbb"

seen = {}
left = 0
max_length = 0

for right in range(len(s)):
    
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    max_length = max(max_length, right-left+1)

print(max_length)


