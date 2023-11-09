class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def vehicle_brand(self):
        return f"Brand: {self.brand}"
    
    def vehicle_model(self):
        return f"Model: {self.model}"
    
    def vehicle_year(self):
        return f"Year: {self.year}"
if __name__ == "__main__":
    car = Vehicle("Porsche", "911", 2023)
    print(car.vehicle_brand())  
    print(car.vehicle_model())  
    print(car.vehicle_year())   




