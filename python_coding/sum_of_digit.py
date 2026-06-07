# sum of digit

num = input("Enter the no. : ")

sum_of_digit = 0

if num.lstrip("+-").isdigit():
    for digit in num:
        i = int(digit)
        sum_of_digit += i
    print("Sum: ", sum_of_digit)
else:
    print("Invalid Input")