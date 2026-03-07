#Ex 1
def print_top_five_numbers():
    numbers = []
    while True:
        user_input = input("Nhập một số (để trống để dừng): ")
        if user_input == "":
            break
        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
            
    numbers.sort(reverse=True)
    print("5 số lớn nhất là:")
    for num in numbers[:5]:
        print(num)
#Ex 2
def print_season():
    seasons = ("winter", "spring", "summer", "autumn")

    try:
        month = int(input("Nhập số của tháng (1-12): "))
        if 1 <= month <= 12:
            season_index = (month % 12) // 3
            print(f"Mùa tương ứng là: {seasons[season_index]}")
        else:
            print("Tháng không hợp lệ!")
    except ValueError:
        print("Vui lòng nhập một số nguyên.")

#Ex 3
def track_names():
    names_set = set()
    
    while True:
        name = input("Nhập tên (để trống để dừng): ")
        if name == "":
            break
            
        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)
            
    print("\nDanh sách các tên đã nhập:")
    for name in names_set:
        print(name)

#Ex 4
def word_frequency(text: str) -> dict:
    words = text.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
        
    return frequency

#Ex 5
def remove_odd_numbers(numbers: list) -> list:
    return [num for num in numbers if num % 2 == 0]

if __name__ == "__main__":
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens_only = remove_odd_numbers(original)
    
    print(f"Original list: {original}")
    print(f"Cut-down list: {evens_only}")

#Ex 6
import random

def approximate_pi():
    try:
        N = int(input("Nhập số lượng điểm ngẫu nhiên để tạo (VD: 1000000): "))
    except ValueError:
        print("Vui lòng nhập số nguyên.")
        return

    n = 0
    
    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if (x**2 + y**2) < 1:
            n += 1

    pi_approx = 4 * n / N
    print(f"Giá trị xấp xỉ của Pi với {N} điểm là: {pi_approx}")