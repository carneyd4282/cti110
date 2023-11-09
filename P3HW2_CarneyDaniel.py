# CTI-110
# P3HW2 - Salary
# Daniel Carney
# 2023-10-12
#

# input name
# input hours
# input pay_rate
# if hours > 40:
#   set overtime_hours to hours - 40
#   set overtime_pay to (overtime_hours * pay_rate * 1.5)
#   set reghour_pay to (pay_rate * 40)
# else:
#   set overtime_hours to 0
#   set overtime_pay to 0
#   set reghour_pay to (pay_rate * hours)
# set gross_pay to overtime_pay + reghour_pay
# print name
# print a bunch of lines
# print hours, pay_rate, overtime_hours, overtime_pay, reghour_pay, gross_pay

def inputVars():
    global name
    global hours
    global pay_rate
    name = input("Enter employee's name: ")
    hours = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

def calcVars():
    global overtime_hours
    global overtime_pay
    global reghour_pay
    global gross_pay
    if hours > 40:
        overtime_hours = (hours - 40)
        overtime_pay = (overtime_hours * pay_rate * 1.5)
        reghour_pay = (40 * pay_rate)
        gross_pay = (overtime_pay) + (reghour_pay)
    else:
        overtime_hours = 0
        overtime_pay = 0
        reghour_pay = (hours * pay_rate)
        gross_pay = reghour_pay

def outputVars():
    print('-'*40)
    print('Employee name: ', name, '\n')
    print(f'{"Hours Worked":<16}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<16}{"RegHour Pay":<15}{"Gross Pay":<9}')
    print('-'*80)
    print(f'{hours:<16}${pay_rate:<11.2f}{overtime_hours:<12}${overtime_pay:<15.2f}${reghour_pay:<14.2f}${gross_pay:<8.2f}')
    
#this is kind of a terrible way to use functions isn't it, but eh, slightly more organized at least
def main():
    inputVars()
    calcVars()
    outputVars()

main()
