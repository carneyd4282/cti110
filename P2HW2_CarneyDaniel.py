# CTI-110
# P2HW2 - List
# Daniel Carney
# 2023-09-19

# make grade list
# get input for module 1 grade and put as 1st place in list
# get input for module 2 grade and put as 2nd place in list
# get input for module 3 grade and put as 3rd place in list
# get input for module 4 grade and put as 4th place in list
# get input for module 5 grade and put as 5th place in list
# get input for module 6 grade and put as 6th place in list
# print "(newline)------------Results------------"
# print lowest grade
# print highest grade
# print sum of grades
# print average of grades
# print closing string of ---

grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

print('\n'+('-'*12)+'Results'+('-'*12))
print('Lowest Grade:      ', min(grades))
print('Highest Grade:     ', max(grades))
print('Sum of Grades:     ', sum(grades))
print(f'Average:            {sum(grades)/len(grades):.2f}')
print('-'*40)
