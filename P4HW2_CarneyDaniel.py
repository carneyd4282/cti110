# CTI-110
# P3HW2 - Salary Calculator
# Daniel Carney
# 2023-11-07
#

#define main function:
#   set all_employee_names_list to empty list
#   set all_hours_worked_list to empty list
#   set all_pay_rates_list to empty list
#   set all_overtime_hours_list to empty list
#   set all_overtime_pay_list to empty list
#   set all_reghour_pay_list to empty list
#   set all_gross_pay_list to empty list
#   set next_employee to result of getEmployeeInfo function
#   while next_employee does not equal 'done':
#       call displayEmployeeInfo function with next_employee
#       append next_employee[0] to all_employee_names_list
#       append next_employee[1] to all_hours_worked_list
#       append next_employee[2] to all_pay_rates_list
#       append next_employee[3] to all_overtime_hours_list
#       append next_employee[4] to all_overtime_pay_list
#       append next_employee[5] to all_reghour_pay_list
#       append next_employee[6] to all_gross_pay_list
#       set next_employee to result of getEmployeeInfo function
#   call printStats function with (all_employee_names_list, all_hours_worked_list, all_pay_rates_list, all_overtime_hours_list, all_overtime_pay_list, all_reghour_pay_list, all_gross_pay_list)
#
#define getEmployeeInfo function:
#   input name
#   if name is 'done':
#       return 'done'
#   input hours
#   input pay_rate
#   if hours > 40:
#       set overtime_hours to hours - 40
#       set overtime_pay to (overtime_hours * pay_rate * 1.5)
#       set reghour_pay to (pay_rate * 40)
#   else:
#       set overtime_hours to 0
#       set overtime_pay to 0
#       set reghour_pay to (pay_rate * hours)
#   set gross_pay to overtime_pay + reghour_pay
#   return [name, hours, pay_rate, overtime_hours, overtime_pay, reghour_pay, gross_pay]
#
#define displayEmployeeInfo function with argument employee_info:
#   print employeee name
#   print headers for hours worked, pay rate, overtime pay, reghour pay, and gross pay
#   print -------------------------------------------------------------------------------------
#   print variables employee_info[0], employee_info[1], employee_info[2], employee_info[3], employee_info[4], employee_info[5], employee_info[6]
#
#define getStats function with arguments (employee_names_list, hours_worked_list, pay_rates_list, overtime_hours_list, overtime_pay_list, reghour_pay_list, gross_pay_list):
#   set num_employees to length of employee_names_list
#   set total_overtime_pay to sum of overtime_pay_list
#   set total_reghour_pay to sum of reghour_pay_list
#   set total_gross_pay to sum of gross_pay_list
#   print num_employees
#   print total_overtime_pay
#   print total_reghour_pay
#   print total_gross_pay
#
#call main function

#could do the unnecessry list-using parts of this slightly more conveniently with dictionaries and/or named tuples but i wasn't sure if we went over that in class or just in zybooks

def getEmployeeInfo():
    name = input("\nEnter employee's name or \"Done\" to terminate: ")
    if (name == 'Done') or (name == 'done'):
        return 'done'
    hours = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))
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
    return [name, hours, pay_rate, overtime_hours, overtime_pay, reghour_pay, gross_pay]

def displayEmployeeInfo(employee_info):
    print('\nEmployee name: ', employee_info[0], '\n')
    print(f'{"Hours Worked":<16}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<16}{"RegHour Pay":<15}{"Gross Pay":<9}')
    print('-'*80)
    print(f'{employee_info[1]:<16}${employee_info[2]:<11.2f}{employee_info[3]:<12}${employee_info[4]:<15.2f}${employee_info[5]:<14.2f}${employee_info[6]:<8.2f}')

def printStats(employee_names_list, hours_worked_list, pay_rates_list, overtime_hours_list, overtime_pay_list, reghour_pay_list, gross_pay_list):
    num_employees = len(employee_names_list)
    total_overtime_pay = sum(overtime_pay_list)
    total_reghour_pay = sum(reghour_pay_list)
    total_gross_pay = sum(gross_pay_list)
    print('\nTotal amount of employees entered:', num_employees)
    print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
    print(f'Total amount paid for regular hours: ${total_reghour_pay:.2f}')
    print(f'Total amount paid in gross: ${total_gross_pay:.2f}')

def main():
    all_employee_names_list = []
    all_hours_worked_list = []
    all_pay_rates_list = []
    all_overtime_hours_list = []
    all_overtime_pay_list = []
    all_reghour_pay_list = []
    all_gross_pay_list = []
    next_employee = getEmployeeInfo()
    while next_employee != 'done':
        displayEmployeeInfo(next_employee)
        all_employee_names_list.append(next_employee[0])
        all_hours_worked_list.append(next_employee[1])
        all_pay_rates_list.append(next_employee[2])
        all_overtime_hours_list.append(next_employee[3])
        all_overtime_pay_list.append(next_employee[4])
        all_reghour_pay_list.append(next_employee[5])
        all_gross_pay_list.append(next_employee[6])
        next_employee = getEmployeeInfo()
    printStats(all_employee_names_list, all_hours_worked_list, all_pay_rates_list, all_overtime_hours_list, all_overtime_pay_list, all_reghour_pay_list, all_gross_pay_list)

main()
