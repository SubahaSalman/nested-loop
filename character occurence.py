string = str(input("Please enter your word: "))
character = input("Please enter your character: ")
i = 0
count = 0

while (i < len(string)):
    if (string[i] == character):
        count = count + 1
    i = i + 1

print("The total number of times the character", character, "has appeared is", count)