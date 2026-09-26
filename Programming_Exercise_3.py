from functools import reduce

num_expenses = int(input("Enter the number of expenses you have: "))

expenses = []

for i in range(num_expenses):
    type = input(f"Enter expense #{i + 1}: ")
    cost = float(input(f"Enter cost for {type}: $"))

    expenses.append((type, cost))

total_expenses = reduce(
    lambda total, expense: total  + expense[1], expenses, 0
)

highest_expense = reduce(
    lambda highest, expense: expense if expense[1] > highest[1] else highest, expenses
)

lowest_expense = reduce(
    lambda lowest, expense: expense if expense[1] < lowest[1] else lowest, expenses
)

print("\n   Total expenses  ")
print(f"Total expenses: {total_expenses:.2f}")
print(f"Highest expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")