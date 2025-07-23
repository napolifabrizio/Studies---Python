from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


# Product
class Car:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {self.parts}", end="")


# Builder abstrato
class CarBuilder(ABC):
    @abstractmethod
    def reset(self) -> None: pass

    @abstractmethod
    def set_model(self, model: str) -> None: pass

    @abstractmethod
    def set_engine(self, engine: str) -> None: pass

    @abstractmethod
    def set_seats(self, number: int) -> None: pass

    @abstractmethod
    def add_gps(self) -> None: pass

    @abstractmethod
    def paint(self, color: str) -> None: pass

    @abstractmethod
    def add_sunroof(self) -> None: pass

    @property
    @abstractmethod
    def car(self) -> Car: pass


# Concrete Builder
class ConcreteCarBuilder(CarBuilder):
    def __init__(self) -> None:
        self._car = None
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def set_model(self, model: str) -> None:
        self._car.add({"Model": model})

    def set_engine(self, engine: str) -> None:
        self._car.add({"Engine": engine})

    def set_seats(self, number: int) -> None:
        self._car.add({"Number": number})

    def add_gps(self) -> None:
        self._car.add({"Gps": True})

    def paint(self, color: str) -> None:
        self._car.add({"Color": color})

    def add_sunroof(self) -> None:
        self._car.add({"Sunroof": True})

    @property
    def car(self) -> Car:
        car = self._car
        self.reset()
        return car


# Director (opcional)
class CarDirector:
    def __init__(self) -> None:
        self._builder: CarBuilder = None

    @property
    def builder(self) -> CarBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: CarBuilder) -> None:
        self._builder = builder

    def build_sports_car(self) -> None:
        self.builder.set_model("Coupe")
        self.builder.set_engine("V8")
        self.builder.set_seats(2)
        self.builder.add_gps()
        self.builder.paint("Red")
        self.builder.add_sunroof()

    def build_economy_car(self) -> None:
        self.builder.set_model("Hatchback")
        self.builder.set_engine("1.0L")
        self.builder.set_seats(4)
        self.builder.paint("White")


# Client code
if __name__ == "__main__":
    builder = ConcreteCarBuilder()
    director = CarDirector()
    director.builder = builder

    print("Sports Car:")
    director.build_sports_car()
    builder.car.list_parts()

    print("\nEconomy Car:")
    director.build_economy_car()
    builder.car.list_parts()

    print("\nCustom Car:")
    builder.set_model("SUV")
    builder.set_engine("V6")
    builder.set_seats(5)
    builder.add_gps()
    builder.paint("Black")
    builder.car.list_parts()
