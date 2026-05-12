# Input Format

# The first line contains the integer, n .
# The next n lines each contain a word.

# Output Format

# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output

# 3
# 2 1 1
# Explanation

# There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

from collections import Counter


def word_order(order):
    words = order.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) +1
        

    print(len(freq))
    print( *freq.values() )


order = "my name arpan arpan"
word_order(order)
