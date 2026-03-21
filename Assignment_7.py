import random

class Car:
    def __init__(self, registration_number: str, maximum_speed: int):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        
    def accelerate(self, change_of_speed: int):
        self.current_speed += change_of_speed
        
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
            
        if self.current_speed < 0:
            self.current_speed = 0
            
    def drive(self, hours: float):
        distance_this_trip = self.current_speed * hours
        self.travelled_distance += distance_this_trip

if __name__ == "__main__":
    
    print("--- KIỂM TRA XE CƠ BẢN ---")
    my_car = Car("ABC-123", 142)
    print(f"Xe vừa tạo: Biển số {my_car.registration_number}, "
          f"Tốc độ tối đa {my_car.maximum_speed} km/h, "
          f"Tốc độ hiện tại {my_car.current_speed} km/h, "
          f"Đã đi {my_car.travelled_distance} km.")
          
    my_car.accelerate(30)
    my_car.accelerate(70)
    my_car.accelerate(50)
    print(f"Tốc độ sau khi tăng tốc liên tục (giới hạn 142): {my_car.current_speed} km/h")
    
    my_car.accelerate(-200)
    print(f"Tốc độ sau khi phanh khẩn cấp (không rớt xuống dưới 0): {my_car.current_speed} km/h")
    print("\n")

    print("--- BẮT ĐẦU GIẢI ĐUA XE ---")
    cars_list = []
    
    for i in range(1, 11):
        reg_number = f"ABC-{i}"
        max_spd = random.randint(150, 200)
        new_car = Car(reg_number, max_spd)
        cars_list.append(new_car)
        
    race_ongoing = True
    hours_passed = 0
    
    while race_ongoing:
        hours_passed += 1
        
        for car in cars_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            
            car.drive(1)
            
            if car.travelled_distance >= 10000:
                race_ongoing = False
                
    print(f"Cuộc đua kết thúc sau {hours_passed} giờ!\n")
    
    print(f"{'Biển số':<10} | {'Tốc độ Max':<15} | {'Tốc độ cuối':<15} | {'Tổng quãng đường'}")
    print("-" * 65)
    
    for car in cars_list:
        print(f"{car.registration_number:<10} | "
              f"{car.maximum_speed:<10} km/h | "
              f"{car.current_speed:<10} km/h | "
              f"{car.travelled_distance} km")