# leap year


def leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
print(leap_year(2020))  # True
print(leap_year(1900))  # False

