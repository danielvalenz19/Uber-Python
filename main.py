from car import Car
from account import Account

if __name__ == "__main__": 
    print("hola Mundo!")

    car = Car("FDS443", Account("jose aguilar ", "43534"))
    print(vars(car))
    print(vars(car.driver))