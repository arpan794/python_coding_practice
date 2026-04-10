
# text = "hello world"
# capitalized = text.capitalize()
# print(capitalized) # Output: Hello world


# text = "hello world"
# print(text.title())   # Output: Hello World


# text = "hello world"

# # Capitalize first character manually
# if text:
#     capitalized = text[0].upper() + text[1:]
# else:
#     capitalized = ""

# print(capitalized)

#==============================================

text = "hello world from python"

# Split the string into words
words = text.split()

# Capitalize each word manually
capitalized_words = [word[0].upper() + word[1:] if word else "" for word in words]

# Join the words back into a string
result = " ".join(capitalized_words)

print(result)

