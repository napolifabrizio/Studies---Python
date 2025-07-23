



class Car:
    def __init__(self, model, engine, seats, gps, color, sunroof):
        self.model = model
        self.engine = engine
        self.seats = seats
        self.gps = gps
        self.color = color
        self.sunroof = sunroof

    def __str__(self):
        return (f"Model: {self.model}, Engine: {self.engine}, Seats: {self.seats}, "
                f"GPS: {'Yes' if self.gps else 'No'}, Color: {self.color}, "
                f"Sunroof: {'Yes' if self.sunroof else 'No'}")

# Criando um carro
car = Car("Sedan", "V6", 5, True, "Black", False)
print(car)
