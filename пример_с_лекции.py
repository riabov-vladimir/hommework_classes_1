class FourWheelsVehicle:
    wheels = 4
    fuel = None  # litres
    position = 0  #

    def start(self):
        self.state = 'started'
        print('Started!')

    def accelerate(self, value):
        print('piu-piu')
        self.speed += value

    def steer(self, hours):
        print('piu-piu')
        self.position += self.speed * hours
        self.fuel -= 10 * hours  # 10 l/h

    def stop(self):
        self.speed = 0
        self.state = 'stopped'
        print('Stopped')


class ExpensiveMixin:
    cost = 100000000  # $


class Car(FourWheelsVehicle, ExpensiveMixin):
    color = 'blue'
    speed = 0  # km/h
    state = 'stopped'

    def __init__(self, color, fuel, position):
        self.color = color
        self.fuel = fuel
        self.position = position

    def accelerate(self, value):
        print('траляля')
        super().accelerate(value)

    def __gt__(self, other):
        return self.speed > other.speed

# car0 = Car('red', 50, 10)
car1 = Car('blue', 50, 11)
#
# car0.accelerate(10)
# car1.accelerate(20)
#
# print(car0 < car1)


print(Car.__dict__)
print(car1.__dict__)