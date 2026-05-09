
def frequency(str):
    freq = {}

    for ch in str:
        freq[ch] = freq.get(ch, 0) + 1
        
    return freq

s = "interview"
print(frequency(s))