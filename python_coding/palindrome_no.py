# no.  is palindrome

# num = (input("Enter the no. :"))

# if num == num[::-1]:
#     num_int = int(num)
#     print("No. is palindrome")
# else:
#     print("No. is not palindrome")


# first checking the input is integer or not


num = input("Enter the no. :")

if num.isdigit():
    if num == num[::-1]:
        print("No. is palindrome")
    else:
        print("No. is not palindrome")
else:
    print("Invalid Integer")