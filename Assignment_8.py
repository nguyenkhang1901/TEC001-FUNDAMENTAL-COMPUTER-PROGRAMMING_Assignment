import random

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print(f"Elevator is at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor > self.top or target_floor < self.bottom:
            print("Invalid floor!")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for _ in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nRunning elevator {elevator_number} to floor {destination_floor}:")
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\n--- FIRE ALARM! All elevators returning to bottom floor ---")
        for i in range(len(self.elevators)):
            print(f"Elevator {i}:")
            self.elevators[i].go_to_floor(self.bottom)


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = max(0, min(self.maximum_speed, self.current_speed + change))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name} | Distance: {self.distance} km")
        print(f"{'Reg':<10} | {'Max Spd':<10} | {'Cur Spd':<10} | {'Distance'}")
        print("-" * 55)
        for car in self.cars:
            print(f"{car.registration_number:<10} | {car.maximum_speed:<7} km/h | {car.current_speed:<7} km/h | {car.travelled_distance} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


if __name__ == "__main__":
    my_building = Building(0, 10, 3)
    my_building.run_elevator(0, 5)
    my_building.run_elevator(1, 8)
    my_building.fire_alarm()

    car_list = []
    for i in range(1, 11):
        car_list.append(Car(f"ABC-{i}", random.randint(150, 200)))
    
    grand_derby = Race("Grand Demolition Derby", 8000, car_list)
    
    hours_count = 0
    while not grand_derby.race_finished():
        grand_derby.hour_passes()
        hours_count += 1
        if hours_count % 10 == 0:
            print(f"\n--- Status after {hours_count} hours ---")
            grand_derby.print_status()

    print(f"\n--- FINAL RESULTS (Race finished after {hours_count} hours) ---")
    grand_derby.print_status()
