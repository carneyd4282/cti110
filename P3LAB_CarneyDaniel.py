# Determines whether given year is a leap year
# Daniel Carney
# CTI-110
# 2023-10-05

# (do we need to do the comment block for the labs?)

is_leap_year = False
   
input_year = int(input())

if (input_year % 100) == 0:
    if (input_year % 400) == 0:
        is_leap_year = True
    else:
        is_leap_year = False
elif (input_year % 4) == 0:
    is_leap_year = True
else:
    is_leap_year = False

if is_leap_year == True:
    print(input_year, '- leap year')
else:
    print(input_year, '- not a leap year')