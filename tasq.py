# TASKS
import math
# ----1
try:
    price = int(input("Enter the price of the item > "))
    discount = int(input("Enter the discount percentage > "))
except ValueError:
    print("Price/Discount must be an integer.")
finally:
    print("The calculations have been completed.")

# ----2
try:
    dollares = int(input("Enter the amount in dollars: "))
    exchange_rate = float(input("Enter the dollar-euro exchange rate > "))
    if exchange_rate <= 0:
        raise Exception("Exchange rate must be greater than zero.")
    euros = dollares * exchange_rate
    print(f"${dollares} in euros is: {euros:.2f}€")
except ValueError:
    print("Amount/Exchange rate must be a number.")
finally:
    print("The conversion has been completed.")

# ----3
grades = input("Enter the grades separated by spaces > ").split()
try:
    gradelist = map(int, grades)
    average = math.ceil(sum(gradelist) / len(grades))
    print(f"The average grade is: {average}")
except ValueError:
    print("Grades must be integers.")
except ZeroDivisionError:
    print("No grades were entered.")
finally:
    print("Ending the calculation...")

# ----4
balance = 1000
try:
    withdrawal = int(input("Enter the amount to withdraw > "))
    if withdrawal % 10 != 0:
        raise Exception("Incorrect withdrawal amount.")
    if withdrawal > balance:
        raise Exception("Incorrect withdrawal amount.")
except ValueError:
    print("Withdrawal amount must be an integer.")
except Exception as e:
    print(e)
finally:
    print("End of transaction...")

# ----5
try:
    ordernum = input("Enter the order number > ")
    if not ordernum.startswith("ORD"):
        raise Exception("Incorrect number of order.")
    if ordernum[3:].isdigit() is False:
        raise Exception("Incorrect number of order.")
except Exception as e:
    print(e)
finally:
    print("The check has been completed.")

# ----6
numlist = input("Enter a list of numbers separated by spaces > ").split()
reslist = []
for i in numlist:
    try:
        reslist.append(int(i))
    except ValueError:
        print("Incorrect number.")

try:
    print(f"Sum of the numbers: {sum(reslist)}")
    print(f"Average of the numbers: {math.ceil(sum(reslist) / len(reslist))}")
except ZeroDivisionError:
    print("No numbers were entered.")
finally:
    print("Data has been processed.")
