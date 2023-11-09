# This program takes a number grade, determines average and displays letter grade for average.
# CTI-110
# Daniel Carney
# 2023-10-03

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest, sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
average = total / len(grades)

# print results

print('\n'+('-'*12)+'Results'+('-'*12))
print('Lowest Grade:      ', low)
print('Highest Grade:     ', high)
print('Sum of Grades:     ', total)
print(f'Average:            {average:.2f}')
print('-'*40)

# determine letter grade for average

if average >= 90:
    print('Your grade is: A')
elif 90 > average >= 80:
    print('Your grade is: B')
elif 80 > average >= 70:
    print('Your grade is: C')
elif 70 > average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
