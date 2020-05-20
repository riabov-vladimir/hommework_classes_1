from abc import ABC, abstractmethod

class Creature(ABC):
  age = 0 # новорождённое существо
  weight = 0 # у каждого существа есть вес
  hunger = 'hungry' # допустим каждое существо изначально голодное,
  vaccine = 'not vaccinated' # существа рождаются непривитыми, им можно делать прививки методом vaccinate()

  def __init__(self, name, gender, weight):
    self.name = name
    self.gender = gender
    self.weight = weight

  def say_hi(self):
    print(f'{self.name} says "{self.talk}"')

  def feed(self):
    self.hunger = 'fed'
    print(f'{self.name} is fed!')

  def vaccinate(self):
    self.vaccine = 'vaccinated'
    print(self.name, 'is vaccinated now! More unlikely to get sick')
  @abstractmethod
  def gather(self):
    pass
# if isinstance(self, Bird):
#   self.eggs = 0
# elif isinstance(self, Cow or Goat):
#   self.milk = 0
# elif isinstance(self, Sheep):
#   self.wool = 0

# def goods(self): # переделать
# if isinstance(self, Bird):
#   if self.gender == 'female':
#     print(f'{self.name} снесла {self.eggs} яиц')
# elif isinstance(self, Cow):
#   print(f'C {self.name[:-1]}и можно собрать {self.milk}л молока')
# elif isinstance(self, Sheep):
#   print(f'{self.name} стал очень лохматый! С него можно собрать {self.wool}дцм^3 шерсти')
# elif isinstance(self, Goat):
#   print(f'C {self.name} можно собрать {self.milk}л молока')

  def __gt__(self, other):
    return self.weight > other.weight

  def __add__(self, other):
    return self.weight + other.weight

class Bird(Creature):


  def gather(self):
    self.eggs = 0

class Animal(Creature):
  def get_milk(self):
    self.milk = 0

class Goose(Bird):
  eggs = 5
  talk = 'Ga-ga-ga!'

class Duck(Bird):
  eggs = 10
  talk = 'Quack-quack!'

class Chicken(Bird):
  eggs = 15
  talk = 'Co-co-co!'

class Sheep(Animal):
  wool = 20
  talk = 'Beeee!'

class Goat(Animal):
  milk = 5
  talk = 'Meeeeeh!'

class Cow(Animal):
  milk = 10
  talk = 'Moooo!'

cow1 = Cow('Манька', 'female', 300)
goat1 = Goat('Рога', 'male', 89)
goat2 = Goat('Копыта', 'male', 92)
sheep1 = Sheep('Барашек', 'male', 118)
sheep2 = Sheep('Кудрявый', 'male', 109)
chicken1 = Chicken('Ко-Ко', 'female', 3)
chicken2 = Chicken('Кукареку', 'male', 4)
duck1 = Duck('Кряква', 'female', 3)
goose1 = Goose('Серый', 'male', 5)
goose2 = Goose('Белый', 'male', 5)

creatures_list = [cow1, goat1, goat2, sheep1, sheep2, chicken1, chicken2, duck1, goose1, goose2]

def main():

  while True:
    user_input = input('Что мне сделать, дядюшка Джо? ')
    if user_input == 'hi':
      hi(class_instances)
    elif user_input == 'is hungry':
      check_hunger(class_instances)
    elif user_input == 'feed':
      dinner(class_instances)
    elif user_input == 'gather':
      gather(class_instances)
    elif user_input == 'check goods':
      goods(class_instances)
    elif user_input == 'stats':
      stats(creatures_list)
    elif user_input == 'check vaccine':
      check_vaccination(class_instances)
    elif user_input == 'vaccinate':
      vaccination(class_instances)
    elif user_input == 'bye':
      print('Спасибо за помощь! Увидимся следующим летом!')
      break

def stats(creatures_list):
  print(f'Самое тяжелое из них - {max(creatures_list).name}, {max(creatures_list).weight} кг')
  total_weight = []
  for creature in creatures_list:
    total_weight.append(creature.weight)
  print(f'Общий вес всех животных - {sum(total_weight)}')


def hi(creatures=creatures_list):

  for creature in creatures:
    creature.say_hi()
  print('А я им в ответ: "Привет зверушки!"')

def check_hunger(creatures=creatures_list):
  for creature in creatures:
    print(f'{creature.name} - {creature.hunger}')

def dinner(creatures=creatures_list):
  for creature in creatures:
    creature.feed()

def gather(creatures=creatures_list):
  for creature in creatures:
    creature.gather()

def goods(creatures=creatures_list):
  for creature in creatures:
    creature.goods()

def vaccination(creatures=creatures_list):
  for creature in creatures:
    creature.vaccinate()

def check_vaccination(creatures=creatures_list):
  for creature in creatures:
    print(f'{creature.name} - {creature.vaccine}')

    def filtered_creature_list(target_class):
      class_instances = []
      for creature in creatures_list:
        if isinstance(creature, target_class) == True:
          class_instances.append(creature)
          print('Работаем с:', *map(lambda x: x.name, class_instances), sep=', ')
          return class_instances

def filter_creatures_list():
  user_input = input('C какими зверушками будем взаимодействовать? ')

  while True:
    if user_input == 'млекопитающие':
      target_class = Animal
      break
    elif user_input == 'птицы':
      target_class = Bird
      break
    elif user_input == 'коровы':
      target_class = Cow
      break
    elif user_input == 'козы':
      target_class = Goat
      break
    elif user_input == 'овцы':
      target_class = Sheep
      break
    elif user_input == 'гуси':
      target_class = Goose
      break
    elif user_input == 'утки':
      target_class = Duck
      break
    elif user_input == 'курицы':
      target_class = Chicken
      break
    elif user_input == 'все':
      target_class = Creature
      break
    else:
      target_class = Creature
      break
  return target_class

def class_list(creatures_list, target_class):

  class_instances = []
  for creature in creatures_list:
    if isinstance(creature, target_class) == True:
      class_instances.append(creature)
  print(*map(lambda x: x.name, class_instances))
  return class_instances


target_class = filter_creatures_list()

class_instances = class_list(creatures_list, target_class)

main()