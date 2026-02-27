#Ex 1
def valid_code (code):
    if len(code) != 6:
        return False
    for i in range (3):
        if not code[i].isupper():
            return False
    for i in range(3, 6):
        if not code[i].isdigit():
            return False
    return True

#Ex 2
def valid_color (color):
    if len(color) != 7:
        return False
    if color[0] != '#':
        return False
    valid_character = "0123456789ABCDEFabcdef"
    for i in range (1,7):
        if color[i] not in valid_character:
            return False
    return True
#Ex 3
def sum_numbers_in_text(text):
    total = 0
    current_number = ""
    
    for char in text:
        if char.isdigit():
            current_number += char
        else:
            if current_number != "":
                total += int(current_number)
                current_number = ""

    if current_number != "":
        total += int(current_number)
    
    return total

#Ex 4
def phone_numbers(phone):
    words = phone.split()
    result = []

    for word in words:
        if len(word) == 10 and word.isdigit():
            result.append("[REDACTED]")
        elif word.startswith("+84") and word[3:].isdigit():
            result.append("[REDACTED]")
        else:
            result.append(word)
    return " ".join(result)

print(valid_code("TEC001"))

print(valid_color("#FFA07A"))

text = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
print(sum_numbers_in_text(text))

text2 = "Call me at 0912345678 or +84987654321 tomorrow."
print(phone_numbers(text2))