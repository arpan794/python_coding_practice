def count_occurrence(s, char):
    count = 0

    for ch in s:
        if ch == char:
            count += 1

    return count

s = "hello world"
char = 'o'
occurrence = count_occurrence(s, char)
print(f"The character '{char}' occurs {occurrence} times in the string '{s}'.")


# def count_occurrence(s, char):
#     return s.count(char)


# ⏱️ Complexity
# Approach	Time	Space
# Dictionary	O(n)	O(n)
# Loop	O(n)	O(1)
# Built-in	O(n)	O(1)