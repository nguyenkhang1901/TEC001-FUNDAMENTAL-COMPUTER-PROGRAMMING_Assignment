# Task 1: Zander Size
length = float(input("Enter the length of the zander in cm: "))
size_limit = 42

if length < size_limit:
    difference = size_limit - length
    print("Please release the fish back into the lake.")
    print(f"The fish is {difference:.1f} cm below the size limit.")
else:
    print("The fish meets the size limit. You can keep it!")

# Task 2: Cabin Class
cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()

if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("windowless cabin above the car deck.")
elif cabin_class == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")


# Task 3: Hemoglobin
gender = input("Enter your biological sex (female/male): ").lower()
hg_value = float(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if hg_value < 117:
        print("Hemoglobin value is low.")
    elif 117 <= hg_value <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if hg_value < 134:
        print("Hemoglobin value is low.")
    elif 134 <= hg_value <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender input.")

# Task 4: Leap Year
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Task 5: Pizza Unit Price Calculator
import math
def calculate_unit_price(diameter_cm, price_usd):
    radius_cm = diameter_cm / 2
    area_cm2 = math.pi * (radius_cm ** 2)
    area_m2 = area_cm2 / 10000
    unit_price = price_usd / area_m2
    return unit_price

print("--- Pizza 1 ---")
d1 = float(input("Enter diameter of Pizza 1 (cm): "))
p1 = float(input("Enter price of Pizza 1 (USD): "))

print("--- Pizza 2 ---")
d2 = float(input("Enter diameter of Pizza 2 (cm): "))
p2 = float(input("Enter price of Pizza 2 (USD): "))

unit_price1 = calculate_unit_price(d1, p1)
unit_price2 = calculate_unit_price(d2, p2)

print(f"\nPizza 1 unit price: ${unit_price1:.2f} per sqm")
print(f"Pizza 2 unit price: ${unit_price2:.2f} per sqm")

if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money.")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas offer the same value.")