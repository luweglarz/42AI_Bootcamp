import time
from getpass import getuser
from random import randint
import os


def log(func):
    def inner(*args, **kwargs):
        retfunc = func(*args, **kwargs)
        start = time.time()
        fname = func.__name__
        time.sleep(0.01)
        end = time.time()
        actual = end - start
        with open('machine.log', 'a+') as f:
            f.write(
                f'{getuser()} {fname} [ exec-time =  {actual:.3f} ms ]\n')
        return retfunc
    return inner


class CoffeeMachine:
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
