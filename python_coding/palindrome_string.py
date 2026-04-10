# def palindrome_string(s):

#     cleaned_s = s.replace(" ", "").lower()
#     return cleaned_s == cleaned_s[::-1]

# print(palindrome_string("A man a plan a canal Panama"))


def palindrome_string(s):
    cleaned_s = s.replace(" ", "").lower()
    left = 0
    right = len(cleaned_s) - 1

    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left +=1
        right -=1
    return True

print(palindrome_string("A man a plan a canal Panama"))