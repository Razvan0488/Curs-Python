'''1. a) Creati un context manager care genereaza in mod aleatoriu o lungime si o latime pentru un dreptunghi.
Calculati si printati aria dreptunghiului in interiorul context managerului.
b) Modificati codul astfel in cat se se permita rularea si cu valori predefinite pentru lungime si latime,
nu doar random
'''
import random
print('\n a)')
class RandomRectangle:
    def __enter__(self):
        self.latime = random.randrange(1,10)
        self.lungime = random.randrange(1,10)
        print(f'')
        return  self
    def arie(self):
        return self.latime*self.lungime
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
rm = RandomRectangle()
with rm:
    print(f'Aria dreptunghiului aleatoriu este {rm.arie()}')

print('\n b)')

class Dreptunghi:
    def __init__(self,lungime, latime):
        self.lungime = lungime
        self.latime = latime
    def __enter__(self):
        return self
    def arie(self):
        return self.lungime*self.latime
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
drept = Dreptunghi(3,4)
with drept:
    print(drept.arie())

'''2. Fiind date urmatoarele functii, scrieti un decorator tva_decorator pt cele 2 functii care sa returneze pretul produsului
 cu TVA adaugat (tva = 19%).

def get_tv_price(price):
    return price

def get_laptop_price(price):
    return price

Ex: print(get_tv_price(2000)) # => 2380
'''
print('\nEx2')


def tva_decorator(original_func):
    def wrapper_func(*args):
        initial_price = original_func(*args)
        final_price = 0.19 * initial_price + initial_price
        print(f"Price with TVA added is {final_price}")
        return final_price

    return wrapper_func


@tva_decorator
def get_tv_price(price):
    print(f"Price of TV is: {price}")
    return price


@tva_decorator
def get_laptop_price(price):
    print(f"Price of laptop is: {price}")
    return price


print(get_tv_price(2000))
print(get_laptop_price(4800))