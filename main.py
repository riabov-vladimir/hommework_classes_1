class Creature:
  age = 0 # новорождённое существо
  weight = 0 # у каждого существа есть вес
  hunger = 'hungry' # допустим каждое существо изначально голодное,
  # его можно покормить методом feed() и тогда оно станет сытым ('fed')
  vaccine = 'not vaccinated' # существа рождаются непривитыми, им можно делать прививки методом vaccinate()

  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    # self.weight = weight

  def say_hi(self):
    print(f'{self.name} says "{self.talk}"')

  def feed(self):
    self.hunger = 'fed'
    print(f'{self.name} is fed!')

  def vaccinate(self):
    self.vaccine = 'vaccinated'
    print(self, 'is vaccinated now! More unlikely to get sick')

  def gather(self):
    if isinstance(self, Bird):
      self.eggs = 0
    elif isinstance(self, Cow or Goat):
      self.milk = 0
    elif isinstance(self, Sheep):
      self.wool = 0


class Bird(Creature):

  eggs = None
  class_name = 'Птица'
  def nest(self):
    self.eggs += 1

  def gather_eggs(self):
    self.eggs = 0


class Animal(Creature):
  class_name = 'Млекопитающее' # прикольно было бы срезом менять окончание при выводе
  def get_milk(self):
    self.milk = 0

class Goose(Bird):
  class_name = 'Гусь'
  weight = 4
  eggs = 5
  talk = 'Ga-ga-ga!'

class Duck(Bird):
  weight = 3
  eggs = 10
  talk = 'Quack-quack!'

class Chicken(Bird):
  weight = 4
  eggs = 15
  talk = 'Co-co-co!'

class Sheep(Animal):
  weight = 120
  wool = 20
  talk = 'Beeee!'

class Goat(Animal):
  weight = 100
  milk = 5
  talk = 'Meeeeeh!'

class Cow(Animal):
  weight = 300
  milk = 10
  talk = 'Moooo!'

cow1 = Cow('Манька', 'female')
goat1 = Goat('Рога', 'male')
goat2 = Goat('Копыта', 'male')
sheep1 = Sheep('Барашек', 'male')
sheep2 = Sheep('Кудрявый', 'male')
chicken1 = Chicken('Ко-Ко', 'female')
chicken2 = Chicken('Кукареку', 'male')
duck1 = Duck('Кряква', 'female')
goose1 = Goose('Серый', 'male')
goose2 = Goose('Белый', 'male')

creatures_list = [cow1, goat1, goat2, sheep1, sheep2, chicken1, chicken2, duck1, goose1, goose2]
classes_list = [Animal, Bird, Cow, Goat, Sheep, Duck, Chicken, Goose]
def main():
  user_input = input('Что мне сделать, дядюшка Джо?')
  while True:
    if user_input == 'hi':
      hi()
    elif user_input == 'hungry':
      check_hunger()
    elif user_input == 'dinner':
      dinner()
    elif user_input == 'bye':
      print('Спасибо за помощь! Увидимся следующим летом!')

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
  return target_class






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

def class_list(creatures_list, target_class): # если не сделаю классный инпут, реализую через main()
  # target_class = classes_list[input('Class index: ')]
  class_instances = []
  for creature in creatures_list:
    if isinstance(creature, target_class) == True:
      class_instances.append(creature)
  print(*map(lambda x: x.name, class_instances))

def vaccination(creatures=creatures_list):
  for creature in creatures:
    creature.vaccinate()

def check_vaccination(creatures=creatures_list):
  for creature in creatures:
    print(f'{creature.name} - {creature.vaccine}')

# for creature in creatures_list:
#   print(f'{creature.name} - {creature.hunger}')
 # подсчёт птиц без user_input !WORKS OK!
target_class = filter_creatures_list()
class_list(creatures_list, target_class)


