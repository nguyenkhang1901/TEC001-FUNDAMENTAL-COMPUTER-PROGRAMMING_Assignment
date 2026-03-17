#Ex1
def get_top_five_numbers():
    numbers = []
    print("5 Số Lớn Nhất")
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == "":
            break
        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    numbers.sort(reverse=True)
    
    print("\nThe five greatest numbers are:")
    for num in numbers[:5]:
        print(num)

#Ex2
def check_prime():
    print("Kiểm tra Số Nguyên Tố")
    try:
        num = int(input("Enter an integer: "))
        if num <= 1:
            print(f"{num} is not a prime number.")
            return
        
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
                
        if is_prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
            
    except ValueError:
        print("Invalid input. Please enter an integer.")

#Ex3
def collect_and_print_cities():
    print("Danh sách Thành Phố")
    cities = []
    
    for i in range(5):
        city = input(f"Enter the name of city {i+1}: ")
        cities.append(city)
        
    print("The cities you entered are:")
    for city in cities:
        print(city)

#Ex4
def sum_of_list(numbers: list) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    print("Tính Tổng Danh Sách")
    my_numbers = [15, 25, 35, 45]
    total = sum_of_list(my_numbers)
    print(f"List of numbers: {my_numbers}")
    print(f"Sum of the numbers: {total}")
#Ex5
def remove_uneven(numbers: list) -> list:
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Main program để test
if __name__ == "__main__":
    print("Loại Bỏ Số Lẻ")
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 22]
    cut_down_list = remove_uneven(original_list)
    
    print(f"Original list: {original_list}")
    print(f"Cut-down list: {cut_down_list}")