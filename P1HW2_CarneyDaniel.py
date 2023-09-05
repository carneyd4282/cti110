# A simple travel expense calculator
# 2023-09-04
# CTI-110 P1HW2 - Travel Expense
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
budget = input('\nEnter Budget: ')
destination = input('\nEnter your travel destination: ')
gas = input('\nHow much do you think you will spend on gas? ')
hotel = input('\nApproximately, how much will you need for the accomodation/hotel? ')
food = input('\nLast, how much do you need for food? ')

print('\n'+('-'*12)+'Travel Expenses'+('-'*12))
print('Location:', destination)
print('Initial Budget:', budget)
print('\nFuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)

total = gas + food + hotel
budget -= total
print('\nRemaining Balance:', budget)
