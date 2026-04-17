from itertools import count


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    con_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count +=1
            else:
                con_count +=1
            
    return vowel_count, con_count
 
s = "Hello World"
vowels, consonants = count_vowels(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")    