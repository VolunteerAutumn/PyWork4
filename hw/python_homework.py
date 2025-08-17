# EXC
# ----1
try:
    a = int(input("Enter the first number > "))
    b = int(input("Enter the second number > "))
    result = a / b
except ValueError:
    print("The numbers must be integers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("Execution completed.")

# ----2
list1 = [10, 20, 30, 40, 50]
indx = input("Enter the index of the element to access > ")

try:
    indx = int(indx)
    print(f"The element at index {indx} is {list1[indx]}.")
except ValueError:
    print("The index must be an integer.")
except IndexError:
    print("Index out of range.")
finally:
    print("Completed.")

# ----3
sells = input("Enter the info about items sold > ")
try:
    sellslist = map(int, sells.split())
    total = sum(sellslist)
    print(f"Total items sold: {total}")
except ValueError:
    print("Please enter valid integers separated by spaces.")
finally:
    print("Processing completed.")

# ----4
num = input("Enter a number > ")
try:
    num = int(num)
    if num < 0:
        raise Exception("It's not possible to calculate the square root of a negative number.")
    print(f"The square root of {num} is {num ** 0.5}.")
except ValueError:
    print("Please enter an integer.")
except Exception as e:
    print(e)
finally:
    print("Completed.")

# ----5
infostring = input("Enter the info about items sold (name, price, amount) > ")

try:
    name, price, amount = infostring.split(", ")
    price = float(price)
    amount = int(amount)
except ValueError:
    print("Please enter the data in the correct format: name, \nprice (floating point number), amount (integer).")
finally:
    print("Data processing completed.")

# ----6
import random
def connect_to_server():
    if random.choice([True, False]):
        print("Connected to the server successfully.")
    else:
        raise ConnectionError("Failed to connect to the server.")
    
try:
    connect_to_server()
except ConnectionError as e:
    print(e)
finally:
    print("Connection attempt finished.")

# EXC2
# ----1
line1 = input("Enter a line of text: ")
line2 = input("Enter another line of text: ")
line3 = input("Enter a third line of text: ")

with open("data.txt", "w") as file:
    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")

# ----2
try:
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for i in range(1, len(lines), 2):
            print(lines[i].strip())
except FileNotFoundError:
    print("The file 'data.txt' does not exist.")

# ----3
with open("data.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        if 'Python' in i:
            with open("filtered.txt", "a") as file_filtered:
                file_filtered.write(i)

# ----4
name = input("Enter the name of the file to clean > ")
with open(name, "r") as file:
    lines = file.readlines()
    with open("cleaned.txt", "w") as file_cleaned:
        # it will remove all numbers from the file and save the result in cleaned.txt without using lambdas
        for line in lines:
            for char in line:
                if not char.isdigit():
                    file_cleaned.write(char)

# ----5
with open("log.txt", "r") as file:
    text = file.read().lower()
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_word_count[:10]  # Only take the top 10 most used words
    with open("word_stats.txt", "w") as file_word_count:
        for word, count in top_10:
            file_word_count.write(f"{word}: {count}\n")

# ----6
with open("data.txt", "r") as file:
    lines = file.readlines()
    with open("reversed.txt", "w") as file_reversed:
        for line in lines[::-1]:
            file_reversed.write(line)
