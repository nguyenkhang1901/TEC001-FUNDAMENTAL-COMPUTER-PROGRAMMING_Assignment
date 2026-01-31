#Ex 1:
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1
#Ex 2:
while True:
    try:
        inches = float(input("Enter inches (enter -1 to quit): "))
        if inches < 0:
            print("Negative value entered. Program ending.")
            break

        cm = inches * 2.54
        print(f"{inches} inches is {cm} cm")
    except ValueError:
        print("Please enter a valid number.")
#Ex 3:
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit and have answer): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("That is not a valid number.")

if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered.")
#Ex 4:
import random
target_number = random.randint(1, 10)

while True:
    # 1. Nhập dữ liệu dưới dạng chuỗi (string) trước
    user_input = input("guess a number (or type end to stop the game): ")

    if user_input == "end":
        print("End the guess")
        break

    try:
        guess = int(user_input)

        if guess == target_number:
            print("Correct")
            break
        elif guess < target_number:
            print("Too low")
        else:
            print("Too high")

    except ValueError:
        # Nếu nhập cái gì đó không phải số (và cũng không phải "end")
        print("Please enter a valid integer.")
#Ex 5:
attempts = 0
max_attempts = 5
success = False
if input ("Would you like to login? (y/n): ") == "y":
    while attempts < max_attempts:
        username = input("Username: ")
        password = input("Password: ")
        if username == "python" and password == "rules":
            print("Welcome")
            success = True
            break
        else:
            attempts += 1
            print(f"Incorrect credentials. Attempts remaining: {max_attempts - attempts}")

    if not success:
        print("Access denied")
else:
    print("stop login")
#Ex 6:
word = input("Enter a word to test: ")
def get_middle_char(text):
    length = len(text)
    mid_index = length // 2

    if length % 2 == 0:
        return text[mid_index - 1: mid_index + 1]
    else:
        return text[mid_index]

print(get_middle_char(word))


#Ex 7:
words = input("Enter a word to test: ")
def create_acronym(phrase):
    words = phrase.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym

print(create_acronym(words)) # Output: UFO
