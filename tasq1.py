# === PART 1 ===
# ----1
with open("output.txt", "w") as file:
    file.write("Hello, World!")

# ----2
with open("output.txt", "r") as file:
    print(file.read())

# ----3
with open("data.txt", "r") as file:
    with open("backup.txt", "w") as backup_file:
        backup_file.write(file.read())

# ----4
with open("data.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    print(f"Number of lines in data.txt: {line_count}")

# ----5
with open("data.txt", "r") as file:
    content = file.read()
    line_count = content.count('\n') + 1
    word_count = len(content.split())
    char_count = len(content)
    print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")

# ----6

listofletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("data.txt", "r") as file:
    content = file.read()
    encrypted_content = ""
    for char in content:
        if char in listofletters:
            index = listofletters.index(char)
            encrypted_content += listofletters[(index + 1) % len(listofletters)]
        else:
            encrypted_content += char
    with open("encrypted.txt", "w") as encrypted_file:
        encrypted_file.write(encrypted_content)

# @Volunteer_Autummn17, all rights reserved.
