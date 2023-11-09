from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year,color):
        super().__init__(brand,model,year)
        self.color = color

    def car_info(self):
        return f" {self.vehicle_brand()} - {self.vehicle_model()} - {self.vehicle_year()} - Color: {self.color}"
    
class Plane(Vehicle):
    def __init__(self, brand, model, year, num_people):
        super().__init__(brand, model, year)
        self.num_people = num_people
    
    def plane_info(self):
        return f"{self.vehicle_brand()} - {self.vehicle_model()} - {self.vehicle_year()} - People: {self.num_people}"

class Boat(Vehicle):
    def __init__(self, brand, model, year, num_passengers):
        super().__init__(brand, model, year)
        self.num_passengers = num_passengers
    
    def boat_info(self):
        return f"{self.vehicle_brand()} - {self.vehicle_model()} - {self.vehicle_year()} - Passengers: {self.num_passengers}"
    
class RaceCar(Car):
    def __init__(self,brand, model, year,color, top_speed):
        super().__init__(brand, model, year,color)
        self.top_speed = top_speed

    def race_car_info(self):
        return f"{self.car_info()} - Top Speed: {self.top_speed} mph"
    

    
"Porsche", "911", 2022, "Silver"
car = Car("Porsche", "911", 2022, "Silver")
print(car.car_info())

plane = Plane("Boeing", "747", 2023, 150)
print(plane.plane_info())

boat = Boat("White Star Line", "Titanic", 1912, 2200)
print(boat.boat_info())

race_car = RaceCar("Ferrari", "458 Italia", 2023, "Yellow", 200)
print(race_car.race_car_info())