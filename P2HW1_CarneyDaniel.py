# A simple travel expense calculator
# 2023-09-09
# CTI-110 P2HW1 - Travel Expense
# Daniel Carney
#

#set budget to user input
#set destination to user input
#set gas to user input
#set hotel to user input
#set food to user input
#print budget, destination, gas, hotel, food
#set total to gas + food + hotel
#subtract total from budget
#print budget

print('This program calculates and displays travel expenses')
budget = float(input('\nEnter Budget: '))
destination = input('\nEnter your travel destination: ')
gas = float(input('\nHow much do you think you will spend on gas? '))
hotel = float(input('\nApproximately, how much will you need for the accomodation/hotel? '))
food = float(input('\nLast, how much do you need for food? '))

print('\n'+('-'*12)+'Travel Expenses'+('-'*12))
print(f'Location:           {destination}')
print(f'Initial Budget:     ${budget:.2f}')
print(f'Fuel:               ${gas:.2f}')
print(f'Accomodation:       ${hotel:.2f}')
print(f'Food:               ${food:.2f}')
print(('-'*12)+('-'*len('Travel Expenses'))+('-'*12))

total = gas + food + hotel
budget -= total
print(f'\nRemaining Balance:  ${budget:.2f}')
