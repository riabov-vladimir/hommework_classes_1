from abc import ABC, abstractmethod


class Animal(ABC):
	# общий метод, который будут использовать все наследники этого класса
	def __init__(self, name):
		self.name = name

	def eating(self):
		print("Все животные едят")

	# абстрактный метод, который будет необходимо переопределять для каждого подкласса
	@abstractmethod
	def animal_voice(self):
		pass

class Cow(Animal):

	def animal_voice(self):
		return 'mooo'


cow1 = Cow('Tiny')
cow2 = Cow('Miny')


print(type(cow1))
print(type(cow2))


print(cow1.animal_voice)
print(cow2.animal_voice())
