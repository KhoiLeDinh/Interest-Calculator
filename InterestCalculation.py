import math
money_deposited = float(input("Enter the amount deposited: "))
rate_of_interest = float(input("Enter the rate of interest:"))
money_goal = float(input("Enter the amount you want to reach:"))
years = 0
while money_deposited < money_goal:
    interest = money_deposited * rate_of_interest / 100
    money_deposited += interest
    years += 1
print("You will reach your goal in", years, "years.")