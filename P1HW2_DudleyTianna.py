# This code will calculate the travel expense, The numbers will be converted to floating-point numbers.
# 10.10.2023
#CTI-110 P1HW2 - Travel Expense
#Tianna Dudley
#
 
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))
expenses = gas + accommodation + food
remaining_budget = budget - expenses


print("-------Travel Expenses------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget}")
print(f"Fuel: ${gas}")
print(f"Accomodation: ${accommodation}")
print(f"Food: ${food}")
print(f"Remaining Balance: ${remaining_budget}")