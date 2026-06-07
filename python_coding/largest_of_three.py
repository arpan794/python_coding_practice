num1 = int(input("Enter the 1st no. :"))
num2 = int(input("Enter the 2nd no. :"))
num3 = int(input("Enter the 3rd no. :"))


if (num1 > num2) and (num1 > num3):
    print(f"num : {num1} is largest")
elif (num2 > num1) and (num2 > num3):
    print(f"num : {num2} is largest")
else:
    print(f"num : {num3} is largest")


# optimize 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print("Largest:", max(a, b, c))