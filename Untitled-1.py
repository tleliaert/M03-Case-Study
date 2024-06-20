# Super class: Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass: Automobile
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        return (f"Vehicle type: {self.vehicle_type}\n"
                f"Year: {self.year}\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Number of doors: {self.doors}\n"
                f"Type of roof: {self.roof}")

def main():
    # Define the vehicle type
    vehicle_type = "car"
    
    # Collect user input
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    
    while True:
        doors = input("Enter the number of doors (2 or 4): ")
        if doors in ['2', '4']:
            break
        print("Invalid input. Please enter either 2 or 4.")

    while True:
        roof = input("Enter the type of roof (solid or sun roof): ")
        if roof in ['solid', 'sun roof']:
            break
        print("Invalid input. Please enter either 'solid' or 'sun roof'.")
    
    # Create an instance of Automobile
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Display the information
    print("\nHere is the information you entered:")
    print(car.display_info())

# Run the main function
if __name__ == "__main__":
    main()
